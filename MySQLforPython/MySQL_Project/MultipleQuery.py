#!/usr/bin/python3.5 

import MySQLdb as mysql 
import optparse 

class MySQLQuery(): 
    def __init__(self): 
        ''' Ceate an instance to form and execute a MySQL statement. ''' 
        self.Statement = [] 
    def type(self, kind):
        ''' Indicate the type of the statement that the instance is. ''' 
        self.type = kind 
    def connection(self):
        HOST = 'localhost' 
        USER = 'root' 
        DATABASE = 'sakila' 
        PW = 'Tv0912548857' 

        try:
            mydb = mysql.connect( HOST, USER, PW, DATABASE ) 
            cur = mydb.cursor() 
            return cur 
        except mysql.Error as e: 
            raise e

    def query(self,value,sample): 
        if sample == 1: 
            if self.type =='actor': 
                statement = "SELECT first_name, last_name film_info FROM actor_info WHERE last_name = '%s'"%(value) 
            else: 
                statement = "SELECT title, actors FROM flim_list WHERE title LIKE = '%s'"%('%'+value+'%') 
                return self.execute( statement, sample ) 
        else: 
            if self.type == 'actor': 
                statement = "SELECT first_name, last_name film_info FROM actor_info WHERE last_name = '%s'"%(value) 
            else: 
                statement = "SELECT title, actors FROM flim_list WHERE title LIKE = '%s'"%('%'+value+'%') 
                results = self.execute( statement, sample ) 
                return results 
    def execute( self, statement, sample ):
        ''' Attempts execution of the statement resulting from MySQLQuery.form() ''' 
        while True:
            try: 
                cursor = self.connection() 
                cursor.execute(statement) 
                if cursor.rowcount == 0: 
                    print("No results found for yuor query.") 
                    break 
                elif sample == 1: 
                    output = cursor.fetchone() 
                    results = self.format(output,sample) 
                    return results 
                else: 
                    output = cursor.fetchmany(1000) 
                    results = self.format(output,sample) 
                    return results 
            except mysql.Error as e: 
                raise e 
            except mysql.Warning: 
                pass 

    def format(self, output, sample): 
        results = '' 
        if sample == 1: 
            if self.type == 'actor':
                data = output[0] + ' ' + output[1] +':' 
                titles = output[2] 
                entry = titles.split(';') 
                data += entry[0].split(':')[1] 
                results += data+'\n' 
                return results 
            else: 
                data = output[0] + ':' 
                actors = output[1] 
                data += output[1] 
                results += data+'\n' 
                return results 
        else: 
            if self.type == 'actor': 
                for record in  output: 
                    actor = record[0] + ' ' + record[1] + ':' 
                    for item in range(2, len(record) ):
                        names = record[item].split(';') 
                        for i in range(len(names)): 
                            if i == 0:
                                title = '\n'+name[i] 
                            else: 
                                title += title+'\n'+name[i] 
                    data = actor + title + '\n' 
                    results = results + data + '\n' 
            else: 
                for record in output: 
                    title = record[0] + ' '
                    for item in range(1,len(record)): 
                        names = record[item].split(',') 
                        for i in range(0,len(names)): 
                            if i == 0: 
                                actor = '\n'+name[i] 
                            else: 
                                actor = actor + '\n' + name[i] 
                    data = title + actor + '\n' 
                    results = results + data + '\n' 
            return results 

def main(): 
    # Add option 
    opt = optparse.OptionParser() 
    opt.add_option( '-a', '--actor', action='store', help='denotes the lastname/surname of the actor for search', dest='actor') 
    opt.add_option( '-f','--film', action='store', help='denotes the film for search', dest = 'film') 
    opt, args = opt.parse_args() 

    # Check the user input 
    status = 0 
    while opt.film and opt.actor: 
        print( "Please specify the column that you want to search. This program don't support search for both." ) 
        status = 1 
        break 

    while status == 0: 
        request = MySQLQuery() 

        try: 
            if opt.actor: 
                request.type('actor')
                value = opt.actor 
            elif opt.film: 
                request.type('film') 
                value = opt.film 
            results = request.query(value,1) 

            if results: 
                print("Sample returns for the search you requested are follow") 
                print(results) 
                confirm = intput("Are these the kind of data that you are seeking?[Y/n]") 

                confirm = confirm.strip() 

                if confirm[0] != 'Y': 
                    print("\nResults not found. Try again!\n") 
                    break 
            if confirm[0] == 'Y': 
                results = request.query(value,0) 
                print("\nResults for you query are as follow.\n") 
                print(results) 
                break 
            else: 
                break 
        except mysql.Error as e: 
            raise e 
        except mysql.Warning: 
            pass 


if __name__ == '__main__': 
    main() 





