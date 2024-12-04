import type { Post } from '@/model/post'

export const mockPosts: Post[] = [
  {
    id: 1,
    userId: 1,
    username: 'JohnDoe',
    content: 'Hello, world! This is my first post.',
    likes: 5,
    comments: [{ username: 'Jane', comment: 'Nice post!' }],
  },
  {
    id: 2,
    userId: 2,
    username: 'JaneDoe',
    content: 'Vue 3 is amazing!',
    likes: 10,
    comments: [
      { username: 'John', comment: 'Totally agree!' },
      { username: 'Alice', comment: 'Indeed!' },
    ],
  },
]

export function fetchPosts(): Promise<Post[]> {
  return new Promise((resolve) => {
    setTimeout(() => resolve(mockPosts), 500)
  })
}

export function createPost(post: Post): Promise<Post> {
  return new Promise((resolve) => {
    mockPosts.push(post)
    setTimeout(() => resolve(post), 500)
  })
}
