<template>
  <div>
    <div
      v-for="comment in commentStore.comments"
      :key="comment.id"
      class="comment bg-light p-3 rounded-3 mb-2"
    >
      <span class="comment-content" data-bs-dismiss="modal">
        <RouterLink :to="`/user/profile/${comment.user.pk}`">
          <img
            :src="
              comment.user.profile_pic ? userProfilePic(comment.user.profile_pic) : AvatarPicSrc
            "
            class="profile-pic"
            alt="Profile Picture"
          />
          <span class="me-2 text-secondary text-decoration-none">
            {{ comment.user.username.split('@')[0] }}
          </span>
        </RouterLink>
        {{ comment.content }}
      </span>
      <button
        v-if="comment.user && userStore.userData.pk === comment.user.pk"
        @click="deleteComment(comment.pk)"
        class="delete-button btn btn-sm btn-outline-secondary"
      >
        <i class="bi bi-trash text-secondary"></i>
      </button>
    </div>
    <div class="comment-input-section d-flex">
      <input
        v-model="newCommentContent"
        placeholder="댓글을 입력하세요..."
        class="comment-input form-control me-2"
      />
      <button @click="createComment" class="comment-submit-button btn btn-info">
        <i class="bi bi-send"></i>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import AvatarSrc from '@/assets/avatar.png'
import { useUserStore } from '@/stores/userStore'
import { useCommentStore } from '@/stores/commentStore'

const props = defineProps(['article'])

const commentStore = useCommentStore()
const userStore = useUserStore()

const AvatarPicSrc = AvatarSrc
const newCommentContent = ref('')

const userProfilePic = (path) => `http://localhost:8000${path}`

const createComment = () => {
  commentStore
    .createNewComment(props.article.movie, props.article.id, {
      content: newCommentContent.value
    })
    .then(() => {
      newCommentContent.value = ''
    })
    .catch((error) => {
      console.error(error)
    })
}

const deleteComment = (commentPk) => {
  commentStore
    .deleteOldComment(props.article.movie, props.article.id, commentPk)
    .then(() => {})
    .catch((error) => {
      console.error(error)
    })
}

onMounted(() => {
  const movieId = props.article.movie?.pk ?? props.article.movie
  commentStore.initializeComments(movieId, props.article.id)
})
</script>

<style scoped>
.comment {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.comment-content {
  flex: 1;
}
.comment-content a {
  text-decoration: none;
}
.delete-button {
  margin-left: 1rem;
}

.comment-input-section {
  display: flex;
  margin-top: 1rem;
}

.comment-input {
  flex: 1;
}
.profile-pic {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
  object-fit: cover;
}
</style>
