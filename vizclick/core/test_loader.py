from vizclick.core.ontology_loader import OntologyLoader

loader = OntologyLoader("knowledge")

loader.load()

print(f"Loaded {loader.count()} concepts")
print(loader.categories())

concept = loader.get("lighting.soft_diffused")

print(concept)
print(concept.production_description)