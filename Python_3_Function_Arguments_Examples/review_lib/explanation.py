# None is a special value in Python. It is unique (there can’t be two different Nones) 
# and immutable (you can’t update None or assign new attributes to it).

# None is used to define a variable that you can’t assign a value to yet

# None is falsy, meaning that it evaluates to False in an if statement. 

# None is also unique, which means that you can test if something is None using the is keyword.

none_var = None
if none_var:
  print("Hello!")
else:
  print("Goodbye") 
# Prints "Goodbye"


# first we define session_id as None
session_id = None
 
if session_id is None:
  print("session ID is None!")
  # this prints out "session ID is None!"
 
# we can assign something to session_id
elif active_session:
  session_id = active_session.id
  
# but if there's no active_session, we don't send sensitive data
if session_id is not None:
  send_sensitive_data(session_id)

# We initialize our session_id to None, then set our session_id if there is an active session. 
# Since session_id could either be None we check if session_id is None before sending our sensitive data.
