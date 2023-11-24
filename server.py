import http.server
import socketserver
import cgi
from result_actor import get_results_display
from result_director import get_director_results_display
import sys

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/':
            self.path = 'resources/index.html'

        
        if self.path == '/actor_search':
            self.path = 'resources/actor_search.html'


        if self.path == '/director_search':
            self.path = 'resources/director_search.html'
            

        if self.path == '/summary_search':
            self.path = 'resources/summary_search.html'

        if self.path == '/summary_search':
            self.path = 'resources/summary_search.html'


        if self.path == '/summary_search_top15country':
            self.path = 'resources/summary_search_top15country.html'


        if self.path == '/summary_search_content_year':
            self.path = 'resources/summary_search_content_year.html'

        if self.path == '/summary_search_top_directors':
            self.path = 'resources/summary_search_top_directors.html'

        if self.path == '/summary_search_rating':
            self.path = 'resources/summary_search_rating.html'

        if self.path == '/summary_search_top_actors_movie':
            self.path = 'resources/summary_search_top_actors_movie.html'

        if self.path == '/summary_search_top_actors_show':
            self.path = 'resources/summary_search_top_actors_show.html'
        
        if self.path == '/actor_recent_movies':
            self.path = 'resources/actor_recent_movies.html'
        
        
        
        
        #handle queries 
        if '?' in self.path:
            query_type=self.path.split('?')[0].replace('/','')
            query_param=self.path.split("=")[1]
            print(query_type,query_param)
            print(self.path)

            query_name=query_param.replace('+',' ')
            print(query_name)

            if query_type=='actor_search':
                get_results_display(query_name)
                self.path='resources/actor_search_results.html'

            if query_type=='director_search':
                get_director_results_display(query_name)
                self.path='resources/director_search_results.html'
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    


# Create an object of the above class
handler_object = MyHttpRequestHandler

n = len(sys.argv)

if n != 2:
    print("Incorrect number of arguments")
    exit()

PORT = int(sys.argv[1])
print(PORT)
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()