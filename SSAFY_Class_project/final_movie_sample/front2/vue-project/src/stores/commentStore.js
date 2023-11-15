import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getCommentList, createNewCommentAPI, deleteComment } from '@/apis/movieApi'

export const useCommentStore = defineStore('comment', () => {
  const comments = ref([])

  const initializeComments = (moviePk, articlePk) => {
    getCommentList(moviePk, articlePk)
      .then((response) => {
        if (response && response.data) {
          comments.value = response.data
        }
      })
      .catch((error) => {
        console.error('Error initializing articles:', error)
      })
  }

  const createNewComment = (moviePk, articlePk, payload) => {
    return createNewCommentAPI(moviePk, articlePk, payload)
      .then((response) => {
        if (response.status === 201) {
          comments.value = response.data
        }
      })
      .catch((error) => {
        console.error('Error creating a new comment:', error)
      })
  }

  const deleteOldComment = (moviePk, articlePk, commentPk) => {
    return deleteComment(moviePk, articlePk, commentPk)
      .then((response) => {
        if (response.status === 200) {
          comments.value = response.data
        }
      })
      .catch((error) => {
        console.error('Error deleting an old comment:', error)
      })
  }

  return { comments, initializeComments, createNewComment, deleteOldComment }
})
