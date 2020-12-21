#%%
from diagrams import Cluster, Diagram, Edge


from diagrams.onprem.analytics import Spark
from diagrams.gcp.analytics import *
from diagrams.gcp.database import *
from diagrams.gcp.ml import *
from diagrams.gcp.network import *
from diagrams.gcp.storage import *
from diagrams.gcp.compute import *
from diagrams.gcp.api import *
from diagrams.gcp.devtools import *

from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import *
from diagrams.onprem.analytics import Tableau

from diagrams.generic.device import *
from diagrams.generic.os import *

""" Custom """
from diagrams.custom import Custom


_fname = lambda name: f"outputs/{name}"

config = {
    "title": "",
    "fname": _fname('main')
}

#%%

with Diagram(config["title"],show=False, filename=config["fname"]):
    
   
    
    """ External Sources """

    Imdb = Custom("", "../assets/imdb.png")
    Prime = Custom("", "../assets/prime-dark.png")
    Tmdb = Custom("", "../assets/tmdb.png")
    Kaggle = Custom("", "../assets/kaggle.png")
    ingest = Router("Ingest")
    with Cluster(""):
        
        prep = Dataflow("Cleaning\nPreprocessing")
        ingest>>prep
    
    

    """ Input """
    [Tmdb,Prime]>>Edge(label="Viewer Reported\nData",color='orange')>>ingest
    [Imdb,Kaggle]>>Edge(label="Industry Reported\nData", color='green')>>ingest
    

    

    with Cluster("Data Lake"):
        with Cluster("Accessible"):
            db = [SQL("SQL"),BigTable("Unstructured")]
        dlake = prep>>db>>Storage("Archives")

    
    with Cluster("End to End"):
        
        
        with Cluster("Model\nTesting&Training"):
            models = [GPU(''),
            GPU('')
            ]
        with Cluster("Analysis"):

            with Cluster("Statistical Analysis"):
                stats = prep>>InferenceAPI("Data Team")>>models[0]
            with Cluster("AI/ML"):
                ai = prep>>AdvancedSolutionsLab("Deep Learning")>>models[1]
        
 
    models>>LoadBalancing("Model and Serve")>>[Endpoints("REST API"), Client("Dashboard"), ToolsForVisualStudio("Tools")]
    # with Cluster(" API"):

        
    
   
# %%
