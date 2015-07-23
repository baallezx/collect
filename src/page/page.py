"""
a basic graph object that handles crawling the web for content using basic graph theory.

Example usage:
$ python page.py http://somesite.com ...

`...` dots represent other url links you can enter in
"""
__author__ = "Alexander Balzer <abalzer22@gmail.com>"
__version__ = "0.1.0"

# NOTE: this is a very basic version I wriote at first. I have since modified to be scalable across n nodes that all use a redis cache to sync crawling and placing data in a sharded mongo database

diff_hash = {} # if the value is already in the hash then skip it

# TODO: turn diff_hash into a stronger data structure. because this hash table holds all the graph information for your web pages. you should be able to write this.
# TODO: create multiple ways to traverse through the web. dfs, bfs, user-picked, random, ...
# TODO: add a boolean switch that will tell page if it should recurse or do a single instance.
class page(object):
    """
    a basic webpage object
    """
    def __init__(self,url,parent=None):
        if self.check_hash(url):
            self.url = url #string
#            print "url = ",self.url
            self.parent = parent #string
#            print "parent = ",self.parent
            self.data = self.get_page_data(url) #[strings]
#            print "data = ",self.data
            self.links = self.get_links(self.data) # child nodes
#            print "links = ",self.links
            self.children = self.get_child_nodes(self.links)
#            print "children = ",self.children
            self.filename = None
#            print "filename = ",self.filename

    def get_page_data(self,url):
        """ get the flat plain text for the current page """
        import urllib2
        try:
            return urllib2.urlopen(url).read()
        except:
            # TODO: come up with a resolution for this. (deadlink, javascript, ?script, misspelled)
            # XXX: iterate over ['http','https','git',...] + '://'
            return None

    # TODO: abstract this so that you can get {links: 'a', pics: 'href', ...}
    # TODO: create a recursive method that can get paragraphs inside of body or other element statements, this will allow for deeper digging.
    def get_links(self,data):
        """ get the raw strings of links to the current page """
        import BeautifulSoup as bsp
        try:
            soup = bsp.BeautifulSoup(data)
            return [link['href'] for link in soup.findAll('a',href=True)]
        except:
            return None

# TODO: REOMVE fixed in get_links
    def clean_links(self):
        """ clean the link names to be just the urls """
        if self.links != None:
            new_links = []
            for i in self.links:
                # use a regex to cut out the unneeded stuff
                # new_links.append(cleaned_link)
                pass
            return new_links
        return None

    def get_child_nodes(self,links):
        """ take this pages links and create new page objects that will become 'children' nodes. the reason i used quotes is because that could be left to interpretation. the internet does not move in 1 direction. it is a graph not a tree."""
        self.write_data()
        if isinstance(links,list):
            for i in links:
                if isinstance(i,str) or isinstance(i,unicode):
                    try:
                        child = page(i,self.url)
                        child.write_data(child.url)
                        # TODO: add a new entry to whatever database you are using.
                    except:
                        # TODO: notify you have a failed page. add to some other process to figure out what to do with this link
                        pass

# TODO: write a method to handle cleaning up beautiful soup data. like fetch_all(data,node_token) where node_token=['a','p','h1','h2']

    def write_data(self,location=None):
        """ write data to a specified file location. """
        try:
            if location == None:
                location = "/tmp/scoobydoo.x15"
            w = open(location,"a")
            w.write("\n@~@\n")
            w.write(self.url)
            w.write("\n:::\n")
            for i in self.data:
                w.write(i)
            w.write("\n;;;\n")
            w.write(str(self.children))
            w.write("\n~@~\n")
        except:
            pass

    def save_data(self,db,table):
        """ save data to a mongodb database. """
        try:
            from pymongo import MongoClient as mc
            conn = mc() # default host/port
            # TODO: add remaining database selection and data insertion.
        except:
            return False

    def check_hash(self, val):
        """ check public hash table for a collision so infinite recursion can be caught """
        global diff_hash
        if val in diff_hash:
            return False
        else:
            diff_hash[val] = 0x00 # TODO: set as a pointer to page(object) -or- database pointer.
            return True

	def dump_hash(self,filename):
		""" dump the diff_hash to a json file """
		import json
		global diff_hash
		# TODO: save diff_hash to a json file named filename
# from pymongo import MongoClient as mc
# conn = mc() #default host and port
# conn.port
# conn.database_names()

# [']'|'[']
# |'[']'|'[
# ]'|'[']'|

if __name__ == "__main__":
    import sys
    l = sys.argv[1:]
    n = 0
    for i in l:
        curr_page = page(i)
        curr_page.filename = curr_page.url +"_"+ str(i)
        curr_page.write_data()
