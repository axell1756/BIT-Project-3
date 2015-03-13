import os
import sys
from sqlalchemy import *
engine = create_engine("oracle://gniteckm:.JaPe2006@db-acad.services.coventry.ac.uk:1521/eclive.coventry.ac.uk")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class employee(Base):
__tablename__ = 'employee'
employeeID = Column(int(30), primary_key = True)
name = Column(str(255))
address = Column(str(255))
salary = Column(float(10,2))
associatedProject = Column(int(30))
chargingRate = Column(float(6,2))

class role(Base):
__tablename__ = 'role'
roleID = Column(int(30), primary_key = True)
roletype = Column(str(255))
employeeID = Column(int(30), foreign_key = True)

class resources(Base): 
__tablename__ = 'resources'
resourceid = Column(int, primary_key=True)
resourcename = Column(str(255))
costofresource = Column(int(30))
expensedate = Column(DateTime)

class workpackage(Base):
__tablename__ = 'workpackage'
projectID = Column(int, primary_key=True)
employeeID = Column(int(30), foreign_key = True)
expenses = Column(int(30))
resourceID = Column(int(30), foreign_key = True)
totalActualCosts = Column(DateTime)
totalProjectCost = Column(DateTime)

class emp_wp(Base):
__tablename__ = 'emp_wp'
employeeID = Column(int(30), foreign_key = True)
projectID = Column(int(30), foreign_key = True)
startTime = Column(DateTime)
endTime = Column(DateTime)
actualStartTime = Column(DateTime)
actualEndTime = Column(DateTime)
chargingRate = Column(float(6,2))

class project(Base):
__tablename__ = 'project'
ProjectName = Column(str(255), primary_key = True)
start_time = Column(DateTime)
expectedEndDate = Column(DateTime)
WorkPackage = Column(str(225))
employeeID = Column(int(30))
client = Column(str(255))
projectedProjectCost = Column(float(2,0))

class client(Base):
__tablename__ = 'client'
clientid = Column(int, primary_key=True)
clientname = Column(str(255))
clientaddress = Column(str(255))
budget = Column (int(30))
projectName(str(255))

session.query(employee).all()

