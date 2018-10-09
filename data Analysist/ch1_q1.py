import unicodecsv

def read_csv(name):
    with open(name, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)    

enrollments_filename = './dataset/enrollments.csv'
engagement_filename = './dataset/daily_engagement.csv'
submissions_filename = './dataset/project_submissions.csv'

enrollments = read_csv(enrollments_filename)
engagement = read_csv(engagement_filename)
submissions = read_csv(submissions_filename)

print len(enrollments)
print len(engagement)
print len(submissions)

set_enrollments = set()

for  dic in enrollments:
    print dic



enrollment_num_rows = 0             # Replace this with your code
enrollment_num_unique_students = 0  # Replace this with your code

engagement_num_rows = 0             # Replace this with your code
engagement_num_unique_students = 0  # Replace this with your code

submission_num_rows = 0             # Replace this with your code
submission_num_unique_students = 0  # Replace this with your code