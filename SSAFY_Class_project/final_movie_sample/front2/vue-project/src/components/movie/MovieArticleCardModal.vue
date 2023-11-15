<template>
  <div
    class="modal fade"
    :id="'modal' + article.id"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">{{ article.title }}</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <p v-html="formatContent(article.content)"></p>
          <p data-bs-dismiss="modal">
            <RouterLink :to="`/user/profile/${article.user.pk}`">
              <img
                :src="article.user.profile_pic ? userProfilePic : AvatarSrc"
                class="profile-pic"
                alt="Profile Picture"
              />
              {{ username }}
            </RouterLink>
          </p>
          <p>평점: {{ article.rate }}/10</p>
          <p>작성일: {{ formattedDate }}</p>
          <p>좋아요 : {{ article.like_user_count }}</p>
          <div
            v-if="!isOwner"
            class="like-button-container"
            @click="likeArticle(article.movie, article.id)"
          >
            <i
              :class="isLiked ? 'bi bi-chat-square-heart-fill' : 'bi bi-chat-square-heart'"
              style="font-size: 24px"
            ></i>
          </div>
          <MovieArticleComment :article="article" />
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import AvatarSrc from '@/assets/avatar.png'
import { useUserStore } from '@/stores/userStore'
import { likeArticleApi } from '@/apis/movieApi'
import MovieArticleComment from '@/components/movie/MovieArticleComment.vue'

const props = defineProps(['article'])

const userStore = useUserStore()

const isOwner = computed(() => props.article.user.pk === userStore.userData.pk)
const username = computed(() => props.article.user.username.split('@')[0])
const userProfilePic = computed(() => `http://localhost:8000${props.article.user.profile_pic}`)

// 게시글 좋아요
const isLiked = ref(
  Array.isArray(props.article.like_users)
    ? props.article.like_users.some((user) => user.pk === userStore.userData.pk)
    : false
)

const likeArticle = (moviePk, articlePk) => {
  likeArticleApi(moviePk, articlePk)
    .then((response) => {
      if (response.status === 200) {
        isLiked.value = !isLiked.value
        if (isLiked.value) {
          props.article.like_user_count += 1
        } else {
          props.article.like_user_count -= 1
        }
      } else {
        alert('서버 오류')
      }
    })
    .catch((error) => {
      console.error(error)
    })
}

// 각종 format
const formatContent = (content) => {
  return content.replace(/\n/g, '<br />')
}

const formattedDate = computed(() => {
  let date = new Date(props.article.created_at)
  let year = date.getFullYear()
  let month = ('0' + (date.getMonth() + 1)).slice(-2)
  let day = ('0' + date.getDate()).slice(-2)
  let hours = ('0' + date.getHours()).slice(-2)
  let minutes = ('0' + date.getMinutes()).slice(-2)
  return `${year}-${month}-${day} ${hours}:${minutes}`
})
</script>

<style scoped>
.like-button-container {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  margin: 1rem;
}
.profile-pic {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.modal-dialog {
  max-width: 80%;
}
.modal-body p {
  padding: 1rem;
  margin-bottom: 1rem;
}

.modal-body a {
  color: darkgray;
  text-decoration: none;
}
</style>
