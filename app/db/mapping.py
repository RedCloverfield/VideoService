from app.db.registry import mapper_registry
from app.db.video_table import video_table
from app.models.video_model import Video

mapper_registry.map_imperatively(
    Video,
    video_table
)

mapper_registry.configure()
