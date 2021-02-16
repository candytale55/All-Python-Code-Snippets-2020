
from review_lib import get_next_review, submit_review

# define review 
review = get_next_review()

# Check if there is a review by comparing it against None. If review contains a value that isn’t None, submit it by calling the function submit_review() with review as an argument.

if review is not None:
  submit_review(review)
