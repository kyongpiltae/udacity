import unicodecsv



## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open(enrollments_filename, 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()

def read_csv(name):
    with open(name, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)    

enrollments_filename = './datasets/enrollments.csv'
engagement_filename = './datasets/daily_engagement.csv'
submissions_filename = './datasets/project_submissions.csv'

enrollments = read_csv(enrollments_filename)
print enrollments.__len__

enrollment_num_rows = 0             # Replace this with your code
enrollment_num_unique_students = 0  # Replace this with your code

engagement_num_rows = 0             # Replace this with your code
engagement_num_unique_students = 0  # Replace this with your code

submission_num_rows = 0             # Replace this with your code
submission_num_unique_students = 0  # Replace this with your code