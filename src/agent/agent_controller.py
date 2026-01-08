class AgentController:
    def __init__(self, knowledge_graph, vector_store):
        self.kg = knowledge_graph
        self.vs = vector_store

    def route_query(self, question: str):
        """
        Decide how to answer the question.
        """
        question_lower = question.lower()

        if "skill" in question_lower or "skills" in question_lower:
            return "GRAPH"

        if "suitable" in question_lower or "match" in question_lower:
            return "GRAPH+VECTOR"

        return "VECTOR"

    def answer(self, question: str, candidate_name: str = None):
        route = self.route_query(question)

        if route == "GRAPH":
            if candidate_name:
                skills = self.kg.get_candidate_skills(candidate_name)
                return f"{candidate_name} has the following skills: {skills}"

        if route == "VECTOR":
            results = self.vs.search(question)
            return "\n".join([r.page_content for r in results])

        if route == "GRAPH+VECTOR":
            graph_info = []
            if candidate_name:
                graph_info = self.kg.get_candidate_skills(candidate_name)

            vector_results = self.vs.search(question)

            response = "Candidate skills:\n"
            response += ", ".join(graph_info)
            response += "\n\nRelevant context:\n"

            for r in vector_results:
                response += r.page_content + "\n"

            return response

        return "I could not understand the question."
