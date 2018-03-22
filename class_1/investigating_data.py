import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv("../resources/enrollments.csv")
daily_engagement = read_csv("../resources/daily_engagement.csv")
project_submissions = read_csv("../resources/project_submissions.csv")

### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

def get_unique_students(data):
    unique = set()
    for i in data:
        unique.add(i['account_key'])
    return unique   

#Enrollments

enrollment_num_rows = len(enrollments)
print enrollment_num_rows

enrollment_num_unique_students = len(get_unique_students(enrollments))
print enrollment_num_unique_students

#Daily engagement

engagement_num_rows = len(daily_engagement)
print engagement_num_rows

#Rename the 'Acct' column to 'account_key'
unique_students = set()
for engagement in daily_engagement:
    engagement['account_key'] = engagement['acct']
    del[engagement['acct']]

engagement_num_unique_students = len(get_unique_students(daily_engagement))
print engagement_num_unique_students

#Project submissions

submission_num_rows = len(project_submissions)
print submission_num_rows

submission_num_unique_students = len(get_unique_students(project_submissions))
print submission_num_unique_students

#Missing engagement records

engagement_unique_students = get_unique_students(daily_engagement)

missing_users = []
for user in enrollments:
    user = user['account_key']
    if user not in engagement_unique_students:
        missing_users.append(user)

print 'Missing users: ', len(missing_users)

#Checking for more problems

problems = 0
for enrollment in enrollments:
    user = enrollment['account_key']
    if user not in engagement_unique_students and enrollment['join_date'] != enrollment['cancel_date']:
        problems += 1

print "Problems: " , problems

#Tracking down the remaining problems

udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity'] == "True":
        udacity_test_accounts.add(enrollment['account_key'])

print "Udacity test accounts: ", len(udacity_test_accounts)

def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data



#Refining the question

non_udacity_enrollments = remove_udacity_accounts(enrollments)
print "Non udacity enrollments: ", len(non_udacity_enrollments)

paid_students = {}

for enrollment in non_udacity_enrollments:
    if not enrollment['is_canceled'] or enrollment['days_to_cancel'] > 7:
        account_key = enrollment['account_key']     
        enrollment_date = enrollment['join_date']
        if (account_key not in paid_students or enrollment_date > paid_students[account_key]):
            paid_students[account_key] = enrollment_date   

print len(paid_students)
