import contextlib
@contextlib.contextmanager # we need to import this as a contextmanager

def context_manager(): # create a function
    print("Start Execution") # start of the execution
    yield 10 # how many times will be executed
    print("End Execution") # before this line, the execution will be done


with context_manager() as context: # open the context manager
    print("Execution count is {}".format(context)) # print the execution count


# Context manager in connecting DATABASE

def database(url):
    # setup a connection
    db = postgress.connect(url) #sample database

    yield db # after execute the db it will go here 

    db.disconnect() # then end

url = 'sample.database Address' # import the database __enter__
with database(url) as db: # we're going to use the function to pass in the url then assign it into db name
    course_list = db.execute('SELECT * FROM courses') # access the table from that db
#__exit__
    
# Lets break it down the flow
# 1. the with block in line number 25 will execute and then
# 2. it will go to the database function then execute the db = postgress which is will connect to the database
# 3. then it will yield the db so it will pause there and then it will asign the value of the db back to the WITH block
# 4. it will wait the WITH block to finish after the yield start to execute again
# 5. then it will disconnect the database

# NOTE: the yield will pause the execution of the function until whe WITH block is finish or completed