reports = []
with open("02_input.txt", "r") as file:
    for line in file:
        string_line = line.strip().split()
        int_line = [int(x) for x in string_line]
        reports.append(int_line)

safe_reports_count = 0
unsafe_reports = []
for report in reports:
    good_report = True
    increasing = report[1] > report[0]
    for i in range(1, len(report)):
        difference = report[i] - report[i-1]
        if increasing and difference >= 1 and difference <= 3:
            continue
        if not increasing and difference <= -1 and difference >= -3:
            continue
        else:
            good_report = False
            unsafe_reports.append(report)
            break
    
    if good_report:
        safe_reports_count += 1

print(f" safe_reports_count = {safe_reports_count}")
        
# 463
# correct but bad code!

safe_reports_count = 0
for report in reports:
    differences = []
    bad_report = False
    

    for i in range(1, len(report)):
        differences.append(report[i] - report[i-1])
    
    for i in range(1, len(differences)):
        if differences[i] * differences[i-1] <= 0:
            bad_report = True
            break
    
    if bad_report:
        continue

    for diff in differences:
        if abs(diff) < 1 or abs(diff) > 3:
            bad_report = True
            break
    
    if bad_report:
        continue

    safe_reports_count += 1

print(safe_reports_count)

def count_safe_reports(reports)

        