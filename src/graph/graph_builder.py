import networkx as nx


class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_candidate(self, candidate_name: str):
        self.graph.add_node(candidate_name, type="candidate")

    def add_skill(self, skill: str):
        self.graph.add_node(skill, type="skill")

    def add_role(self, role: str):
        self.graph.add_node(role, type="role")

    def add_candidate_skill(self, candidate: str, skill: str):
        self.graph.add_edge(candidate, skill, relation="HAS_SKILL")

    def add_candidate_role(self, candidate: str, role: str):
        self.graph.add_edge(candidate, role, relation="HAS_ROLE")

    def get_candidate_skills(self, candidate: str):
        return [
            node for node in self.graph.neighbors(candidate)
            if self.graph.nodes[node].get("type") == "skill"
        ]

    def get_graph(self):
        return self.graph
