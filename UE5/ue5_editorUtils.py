import unreal


# takes strings and yields all level actors that contain those strings in their get_name()
def getActorsByNames(*args:str) -> list[actor]:
    for actor in unreal.EditorLevelLibrary.get_all_level_actors():
        if any(string.lower() in lightActor.get_name().lower() for string in *args):
            yield actor

# single line for editor
# [lightActor for lightActor in unreal.EditorLevelLibrary.get_all_level_actors() if any(string.lower() in lightActor.get_name().lower() for string in ["skylight", "skyatmosphere", "directionallight", "exponentialheightfog"])]


# case sensitive
# takes strings and yields all level actors that contain those strings in their get_name()
def getActorsByNamesCS(*args:str) -> list[actor]:
    for actor in unreal.EditorLevelLibrary.get_all_level_actors():
        if any(string in lightActor.get_name().lower() for string in *args):
            yield actor

# single line for editor
# [lightActor for lightActor in unreal.EditorLevelLibrary.get_all_level_actors() if any(string in lightActor.get_name() for string in ["SkyLight", "SkyAtmosphere", "DirectionalLight", "ExponentialHeightFog"])]


# moves the atmospheric actors ["skylight", "skyatmosphere", "directionallight", "exponentialheightfog"] to the coordinates x, y coordinates 0, 0 and up
def moveAtmosphereUp(baseHeight = 3000, heightDelta = 100) -> None:
    for i, actor in enumerate(getActorsByNames("skylight", "skyatmosphere", "directionallight", "exponentialheightfog")):
        actor.set_actor_location(unreal.Vector(0, 0, baseHeight+(heightDelta*i)), False, True)
# single line for editor:
# for i, actor in enumerate([lightActor for lightActor in unreal.EditorLevelLibrary.get_all_level_actors() if any(string.lower() in lightActor.get_name().lower() for string in ["skylight", "skyatmosphere", "directionallight", "exponentialheightfog"])]): actor.set_actor_location(unreal.Vector(0, 0, 3000+(100*i)), False, True)