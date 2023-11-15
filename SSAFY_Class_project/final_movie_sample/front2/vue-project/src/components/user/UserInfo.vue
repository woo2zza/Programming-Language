<template>
  <div class="profile-container bg-light text-dark rounded mt-5 p-4">
    <!-- 프로필 사진 -->
    <div class="profile-pic-container mb-4 text-center">
      <img
        :src="user.profile_pic ? userProfilePic : AvatarSrc"
        alt="No Image"
        class="profile-pic rounded-circle shadow"
      />
    </div>
    <div class="text-center mb-2">
      <button @click="changeProfilePic" class="btn btn-light">프로필 사진 변경</button>
    </div>
    <!-- 사용자 정보 -->
    <div class="text-center mb-4">
      <h3 class="mb-0">{{ username }}</h3>
    </div>
    <div class="user-details border-top pt-3">
      <div class="like-count-info mb-2">
        작성한 기사 수: <strong>{{ user.articles_count }}</strong>
      </div>
      <div class="like-count-info mb-2">
        좋아요 수: <strong>{{ user.like_count }}</strong>
      </div>
      <div class="like-count-info mb-2">
        가입일: <strong>{{ formattedDateJoined }}</strong>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import AvatarSrc from '@/assets/avatar.png'
import { profilePicEdit } from '@/apis/userApi'

const props = defineProps(['user', 'isCurrentUser'])

const username = computed(() => props.user.username.split('@')[0])
const userProfilePic = computed(() => `http://localhost:8000${props.user.profile_pic}`)

// 프로필 사진 변경 logic
const selectedFile = ref(null)

const changeProfilePic = () => {
  const input = document.createElement('input')
  input.type = 'file'
  input.accept = 'image/*'
  input.onchange = (e) => {
    selectedFile.value = e.target.files[0]
    uploadProfilePic()
  }
  input.click()
}

const uploadProfilePic = () => {
  const formData = new FormData()
  formData.append('profile_pic', selectedFile.value)

  profilePicEdit(props.user.id, formData)
    .then((response) => {
      if (response && response.data) {
        props.user.profile_pic = response.data.profile_pic
      } else {
        props.user.profile_pic = URL.createObjectURL(selectedFile.value)
      }
    })
    .catch((error) => {
      console.error(error)
    })
}

const formattedDateJoined = computed(() => {
  const date = new Date(props.user.date_joined)
  return new Intl.DateTimeFormat('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(date)
})
</script>

<style scoped>
.profile-container {
  max-width: 500px;
  min-width: 300px;
  margin: 0 auto;
}

.profile-pic-container {
  position: relative;
}

.profile-pic {
  width: 150px;
  height: 150px;
  object-fit: cover;
}

.user-details .like-count-info {
  font-size: 1.2em;
}
</style>
