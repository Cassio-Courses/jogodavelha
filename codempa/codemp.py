import mysql.connector as bino
tabscomemp=("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'impac' and COLUMN_NAME='codemp' AND TABLE_NAME<>'safemp'")

def consulta():
    bd = bino.connect(host='127.0.0.1', user='root', password='impac123', database='impac')
    cs = bd.cursor()
    tabscomemp = ("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'impac' and COLUMN_NAME='codemp' AND TABLE_NAME<>'safemp'")
    cs.execute(tabscomemp)
    result = cs.fetchall()
    row=int(cs.rowcount)
    for i in range(row):
        cs.execute("update "+str(result[i]).replace("('","").replace("',)","")+" set codemp="+cod+";")
        print("update ",str(result[i]).replace("('","").replace("',)",""),"set codemp="+cod+";")
        bd.commit()
    bd.commit()


cod = input('Digite o numero do codemp\n')
consulta()