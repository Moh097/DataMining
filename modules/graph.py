import networkx as nx
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, kind = "Normal"):
        if kind == "Normal": 
            self.graph = nx.Graph()
        elif kind == "Directed": 
            self.graph = nx.DiGraph()
        self.central = None
        self.labels = {}


    def create_graph(self, student, languages_related, all_languages):

        self.central = student
        self.graph.add_node(student)
        for language in all_languages:
            self.graph.add_node(language)
            
        for language in languages_related:  
            self.graph.add_edge(student, language)
            
    def create_graph_projects(self, cert, cert_student_projects):
        
        self.graph.add_node(cert)
        
        if cert in cert_student_projects:
            related_students = cert_student_projects[cert]

            for student, project_count_weights in related_students.items():
                self.graph.add_edge(cert, student, weight=project_count_weights)
                

    def draw_graph(self, title="graph visualization"):
        if not self.graph:
            print("no graph to visualize")
            return

        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.graph)  
        
        nx.draw(
            self.graph, pos, with_labels=True, 
            node_size=3000, font_size=10, 
            node_color="skyblue", edge_color="gray"
        )
        
        try:
            edge_labels = nx.get_edge_attributes(self.graph, 'weight')
            if edge_labels:
                nx.draw_networkx_edge_labels(
                    self.graph, pos, 
                    edge_labels=edge_labels,
                    font_color="red"
                )
        except KeyError:
            pass
        
        plt.title(title)
        plt.show()

    def clear_graph(self):
        self.graph.clear()
        self.student = None
