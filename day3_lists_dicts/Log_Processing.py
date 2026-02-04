def Log_Processing(logs):
    info_count=0
    errorcount=0
    for log in logs:
        if log.startswith('INFO'):
            info_count+=1
        if log.startswith('ERROR'):
            errorcount+=1
    return info_count,errorcount
print(Log_Processing([
  "INFO login success",
  "ERROR database failed",
  "INFO logout",
  "ERROR timeout",
  "INFO login success"
]))