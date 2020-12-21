#%%
from diagrams import Cluster, Diagram, Edge


from diagrams.onprem.analytics import Spark
from diagrams.gcp.analytics import *
from diagrams.gcp.ml import *
from diagrams.gcp.network import *
from diagrams.gcp.storage import *
from diagrams.gcp.compute import Run
from diagrams.gcp.devtools import Tasks

from diagrams.generic.blank import *

from diagrams.onprem.auth import *
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import *
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import *
from diagrams.onprem.analytics import Tableau

from diagrams.firebase.quality import *
""" Custom """
from diagrams.custom import Custom


_fname = lambda name: f"outputs/{name}"

config = {
    "title": "Data Science as a Service",
    "fname": _fname('abstract')
}

#%%

with Diagram(config["title"],show=False, filename=config["fname"]):
    
   
    
    
    space = Blank('test')
    viewers = Users("Movie Lovers")-space
    with Cluster("Viewer Ship"):
        
        
        

        space - Edge(color="red", style="dotted") - Client("Profile")

 
# %%
