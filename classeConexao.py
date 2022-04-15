import mysql.connector

class Conexao():
    def __init__(self,host,banco,usuario,senha):
        self.host = host
        self.banco = banco
        self.usuario = usuario
        self.senha = senha

    def select(self, pTabela, pCampos, pClausula = ['']):
        conn = mysql.connector.connect(host=self.host,user=self.usuario,database=self.banco,passwd=self.senha)        
        if conn.is_connected():
            cursor = conn.cursor()
            sql = 'SELECT '
            sqlC = ''
            for i in range(0,len(pCampos)):
                sqlC += pCampos[i] + ', ' 
            sqlC = sqlC[:-2] + 'VALUES ('
            sqlV = ' '
            sql += sqlC + ' FROM ' + pTabela
            sqlW = ''            
            if pClausula[0] != '':
                for i in range(0,len(pClausula)):
                    if i == 0:
                        sqlW = ' WHERE ' + pClausula[i]
                    else:
                        sqlW += ' AND ' + pClausula[i]
            # if len(pClausula) != 0:
            #     sql += ' ' + pClausula
            sql += sqlW + ';'
            cursor.execute(sql)
            total = 0
            for linha in cursor:
                total += 1
            if total < 1:
                print(pTabela +' não possui registros!')
            else:
                print('Registros da tabela ' + pTabela)
                cursor.execute(sql)
                for linha in cursor:
                    print(linha)                    
                print('Total de registros: ' + str(cursor.rowcount))
        else:
            print('Não está conectado ao banco de dados')
    
    def insert(self,pTabela,pCampos,pValores):
        conn = mysql.connector.connect(host=self.host,user=self.usuario,database=self.banco,passwd=self.senha)  
        if conn.is_connected():
            cursor = conn.cursor()
            sql = 'INSERT INTO '+ pTabela + ' (' 
            sqlC=' '
            for i in range(0,len(pCampos)):
                sqlC += pCampos[i]+', '
            sqlC = sqlC[:-2] + ') '
            sql += sqlC + ' VALUES ('
            sqlV = ' '
            for i in range (0, len(pValores)):
                if type(pValores[i]) is str:
                    sqlV +='"'+ pValores[i] + '", '
                else:
                    sqlV += str(pValores[i])+ ', '
            sqlV= sqlV[:-2] + '); '
            sql += sqlV
            cursor.execute(sql)
            try:
                conn.commit()
                print('Registro inserido com sucesso')
            except:
                print('Erro ao inserir o registro')
        else:
            print('Não está conectado ao banco de dados')
    
    def delete(self,pTabela,pClausula=['']):
        conn = mysql.connector.connect(host=self.host,user=self.usuario,database=self.banco,passwd=self.senha)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = ' DELETE FROM ' + pTabela
            sqlW = ''
            if pClausula[0] != ' ':
               sql +=' WHERE '
               for i in range(0,len(pClausula)):
                   if i == 0:
                       sqlW = pClausula[i]
                   else:
                        sqlW += ' AND ' + pClausula[i]
            sqlW = sqlW
            sql += sqlW + ';'
            cursor.execute(sql)
            try:
                conn.commit()
                print('Registro excluído com sucesso')
            except:
                print('Erro ao excluir o registro')
        else:
            print('Não está conectado ao banco de dados')
    
    def update(self,pTabela,pCampos,pValores,pClausula=['']):
        conn = mysql.connector.connect(host=self.host,user=self.usuario,database=self.banco,passwd=self.senha)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = ' UPDATE ' + pTabela + ' SET '
            sqlC = ''
            for i in range (0,len(pCampos)):
                if type (pValores[i]) is str:
                    sqlC += pCampos[i] + ' = "' + str(pValores[i]) + '", '
                else:
                    sqlC += pCampos[i] + ' = ' + str(pValores[i]) + ', '
            sqlC = sqlC[:-2] 
            sqlW = ''
            if pClausula[0] != '':
                sqlW = ' WHERE '
                for i in range(0,len(pClausula)):
                    if i == 0:
                        sqlW += pClausula[i]
                    else:
                        sqlW += ' AND ' + pClausula[i]        
            sql += sqlC + sqlW + ';'
            cursor.execute(sql)
            try:
                conn.commit()
                print('Registro alterado com sucesso')
            except:
                print('Erro ao alterar o registro')
        else:
            print('Não está conectado ao banco de dados')

conexao = Conexao('localhost','banco','root','1234')

campos = ['numero_conta_corrente','saldo_conta_corrente']
valores = ['22222',90]
conexao.insert('conta_corrente', campos,valores)

campos = ['numero_conta_corrente','saldo_conta_corrente']
clausula = ['1=1','id_conta_corrente >= 2','numero_conta_corrente != ""']
conexao.select = ('conta_corrente', campos)

campos = ['numero_conta_corrente','saldo_conta_corrente']
valores = ['33333',10.50]
conexao.insert('conta_corrente', campos,valores)

campos = ['*']
conexao.select('conta_corrente',campos)

campos = ['numero_conta_corrente','saldo_conta_corrente']
valores=['55555',45]
clausula = ['numero_conta_corrente = "98765"']
conexao.update('conta_corrente', campos,valores,clausula)

campos = ['*']
conexao.select('conta_corrente',campos)

clausula = ['numero_conta_corrente = "33333"']
conexao.delete('conta_corrente',clausula)

campos = ['*']
conexao.select('conta_corrente',campos)


