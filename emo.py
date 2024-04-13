from fastapi import FastAPI,Depends,status,Response
from . import schemas,models
from .database import engine,sessionLocal
from sqlalchemy.orm import Session
app = FastAPI()
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
models.base.metadata.create_all(engine)
@app.post('/employee')
def create_employee(emp:schemas.Employee,db:Session=Depends(get_db)):
    newEmp = models.Employee(name=emp.name,address=emp.address,mobileNumber=emp.mobileNumber)
    db.add(newEmp)
    db.commit()
    db.refresh(newEmp)
    return newEmp
@app.get('/employee')
def get_emp(db:Session=Depends(get_db)):
    emps = db.query(models.Employee).all()
    return emps
@app.get('/employee/{id}',status_code=200)
def show_emp(id,response:Response, db:Session=Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == id).first()
    if not emp:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail" :f"Employee with the id {id} is not available"}
    return emp
@app.delete('/employee/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_emp(id,response:Response,db:Session=Depends(get_db)):
    emps = db.query(models.Employee).filter(models.Employee.id == id)
    if not emps.first():
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail" :f"Employee with the id {id} is not available"}
    emps.delete(synchronize_session=False)
    db.commit()
    return "deleted"
@app.put('/employee/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_emp(id,emp:schemas.Employee,response:Response,db:Session=Depends(get_db)):
    emps = db.query(models.Employee).filter(models.Employee.id == id)
    if not emps.first():
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail" :f"Employee with the id {id} is not available"}
    emps.update(emp)
    db.commit()
    return "Your record is updated "

