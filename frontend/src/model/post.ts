export interface Post {
  id: number
  userId: number
  username: string
  content: string
  likes: number
  comments: { username: string; comment: string }[]
}
