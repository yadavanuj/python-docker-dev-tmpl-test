from typing import List
from sqlmodel import Session
from app.models import Post


class PostService:
    def __init__(self, session: Session):
        self.session = session

    def create_post(self, post: str) -> Post.Post:
        new_post = Post.Post(post=post)
        self.session.add(new_post)
        self.session.commit()
        self.session.refresh(new_post)
        return new_post

    def get_all_posts(self) -> List[Post.Post]:
        return self.session.query(Post.Post).all()

    def get_post_by_id(self, id: int) -> Post.Post | None:
        return self.session.query(Post.Post).get(id)

    def update_post(self, id: int, post: str) -> Post.Post | None:
        post_obj = self.get_post_by_id(id)
        if post_obj:
            post_obj.post = post
            self.session.commit()
            self.session.refresh(post_obj)
            return post_obj
        return None

    def delete_post(self, id: int) -> bool:
        post_obj = self.get_post_by_id(id)
        if post_obj:
            self.session.delete(post_obj)
            self.session.commit()
            return True
        return False


def create_post_service(session: Session) -> PostService:
    return PostService(session=session)
