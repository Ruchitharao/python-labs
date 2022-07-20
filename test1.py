def apply_flag(row):
    result = ‘’
    if (row[‘REMARK_CODE’] == ‘TRL’):
        result = ‘T’
        elif(row[‘CLOSED_FLAG’] == ‘C’):
        result = ‘C’
        elif(row[‘PAYOFF_DATE’] == None or row[‘PAYOFF_DATE’] != None or row[‘PAYOFF_DATE’] == 0):
        result = ‘P’
        elif(row[‘LAST_PAYMENT_DATE’] or row[‘AMOUNT’] > 0):
        result = ‘S’
        return result

df[‘FLAG’] = df.apply(lambda x: apply_flag(x), axis=1)
