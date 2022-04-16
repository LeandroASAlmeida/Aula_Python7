import constantes as cons
import mysql.connector

class Conexao ():
    def __init__(self, host, banco,usuario,senha):
        self.host = host
        self.banco = banco
        self.usuario = usuario
        self.senha = senha        
        
    def select(self, pTabela, pCampos, pClausula = ['']):
        conn = mysql.connector.connect(host = self.host, user = self.usuario, database = self.banco, password = self.senha)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = 'select '
            sqlC = ''
            for indice in range(0, len(pCampos)):
                sqlC += pCampos[indice] + ', '
            sqlC = sqlC[:-2]
            sql += sqlC + ' from ' + pTabela
            sqlW = ''
            if pClausula[0] != '':
                for indice in range(0,len(pClausula)):
                    if indice == 0:
                        sqlW = ' where ' + pClausula[0]
                    else:
                        sqlW += ' and ' + pClausula[indice]
            sql += sqlW + ';'

            cursor.execute(sql)
            total = 0
            for linha in cursor:
                total += 1
            if total < 1:
                print(pTabela + ' sem registros')
            else:
                print('Registro da tabela ' + pTabela)
                cursor.execute(sql)
                for linha in cursor:
                    print(linha)
                print('Total de registros: '  + str(cursor.rowcount))
        else:
            print(cons.MSG_ERRO_CONEXAO_BD)

    def insert(self, pTabela, pCampos, pValores):
        conn = mysql.connector.connect(host = self.host, user = self.usuario, database = self.banco, password = self.senha)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = 'insert into ' + pTabela + ' ('
            sqlC = ''
            for i in range(0,len(pCampos)):
                sqlC += pCampos[i] + ', '
            sqlC = sqlC[:-2] + ') '
            sql += sqlC + 'values ('
            sqlV = ' '
            for i in range(0, len(pValores)):
                if type(pValores[i]) is str:
                    sqlV += '"' + pValores[i] + '", '
                else:
                    sqlV += str(pValores[i])+ ', '
            sqlV = sqlV[:-2] + '); '
            sql += sqlV

            # sql = 'insert into conta_corrente (numero_conta_corrente, saldo_conta_corrente) values ("12345",0)'
            cursor.execute(sql)
            try:
                conn.commit()
                print('Registro inserido com sucesso!')
            except:
                print('Erro ao inserir registro!!')
        else:
            print(cons.MSG_ERRO_CONEXAO_BD)

    def delete(self, pTabela, pClausula = ['']):
        conn = mysql.connector.connect(host = self.host, user = self.usuario, database = self.banco, password = self.senha)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = 'delete from ' + pTabela
            sqlW = ''
            if pClausula[0] != '':
                sql += ' where '
                for i in range(0, len(pClausula)):
                    if i == 0:
                        sqlW += pClausula[i]
                    else:
                        sqlW += ' and ' + pClausula[i]
            sqlW = sqlW
            sql += sqlW + ';'
            # sql = 'delete from conta_corrente where id_conta_corrente = 4'
            cursor.execute(sql)
            try:
                conn.commit()
                print('Registro excluído com sucesso!!')
            except:
                print('Erro ao excluir o registro!!')
        else:
            print(cons.MSG_ERRO_CONEXAO_BD)

    def update(self, pTabela, pCampos, pValores, pClausula=['']):
        conn = mysql.connector.connect(host = self.host, user = self.usuario, database = self.banco, password = self.senha)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = 'update ' + pTabela + ' set '
            sqlC = ''
            for i in range(0, len(pCampos)):
                if type(pValores[i]) is str:
                    sqlC += pCampos[i] + ' = "' + str(pValores[i]) + '", '
                else:
                    sqlC += pCampos[i] + ' = ' + str(pValores[i]) + ', '
            sqlC = sqlC[:-2]
            sqlW = ''
            if pClausula[0] != '':
                sqlW = ' where '
                for i in range(0, len(pClausula)):
                    if i == 0:
                        sqlW += pClausula[i]
                    else:
                        sqlW += ' and ' + pClausula[i]
            sql += sqlC + sqlW + ';'
            # sql = 'update conta_corrente set numero_conta_corrente = "54321" where id_conta_corrente = 2'
            cursor.execute(sql)
            try:
                conn.commit()
                print('Registro alterado com sucesso!!')
            except:
                print('Erro ao alterar o registro!!')
        else:
            print(cons.MSG_ERRO_CONEXAO_BD)


conexao = Conexao('localhost', 'banco', 'root', '1234')
# conexao.insert()


# clausula = ['id_conta_poupanca = 7', 'numero_conta_poupanca = "23456"']
# conexao.delete('conta_poupanca', clausula)
campos = ['numero_conta_corrente', 'saldo_conta_corrente']
valores = ['22222', 90]
conexao.insert('conta_corrente', campos, valores)

campos = ['numero_conta_corrente', 'saldo_conta_corrente']
clausula = ['1 = 1', 'id_conta_corrente >= 2', 'numero_conta_corrente != ""']
conexao.select('conta_corrente', campos)

campos = ['numero_conta_corrente', 'saldo_conta_corrente']
valores = ['33333', 10.50]
conexao.insert('conta_corrente', campos, valores)

campos = ['*']
conexao.select('conta_corrente', campos)

campos = ['numero_conta_corrente', 'saldo_conta_corrente']
valores = ['55555', 49]
clausula = ['numero_conta_corrente = "33333"']
conexao.update('conta_corrente', campos, valores, clausula)

campos = ['*']
conexao.select('conta_corrente', campos)

clausula = ['numero_conta_corrente = "55555"']
conexao.delete('conta_corrente', clausula)

campos = ['*']
conexao.select('conta_corrente', campos)