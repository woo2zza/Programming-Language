<template>
  <div class="following-info">
    <div class="follow-info row">
      <div class="col-md-5">
        <h6 class="text-center mb-3">팔로워: {{ user.follower_count }}</h6>
        <ul class="list-group mb-4" v-if="user.followers && user.followers.length">
          <li v-for="follower in user.followers" :key="follower.id" class="list-group-item">
            <RouterLink :to="`/user/profile/${follower.id}`">
              <img
                :src="follower.profile_pic ? userProfilePic(follower.profile_pic) : AvatarSrc"
                class="profile-pic"
                alt="Profile Picture"
              />
              <span class="follower-following-name">
                {{ follower.username.split('@')[0] }}
              </span>
            </RouterLink>
          </li>
        </ul>
      </div>
      <div class="col-md-5">
        <h6 class="text-center mb-3">팔로잉: {{ user.following_count }}</h6>
        <ul class="list-group mb-4" v-if="user.followings && user.followings.length">
          <li v-for="following in user.followings" :key="following.id" class="list-group-item">
            <RouterLink :to="`/user/profile/${following.id}`">
              <img
                :src="following.profile_pic ? userProfilePic(following.profile_pic) : AvatarSrc"
                class="profile-pic"
                alt="Profile Picture"
              />
              <span class="follower-following-name"> {{ following.username.split('@')[0] }} </span>
            </RouterLink>
          </li>
        </ul>
      </div>
    </div>
    <button
      v-show="!isCurrentUser"
      :class="isFollowing ? 'btn btn-outline-info mb-5' : 'btn btn-info mb-5'"
      @click="followUnfollow"
      style="width: 130px"
    >
      <i
        :class="isFollowing ? 'bi bi-person-dash' : 'bi bi-person-plus'"
        style="font-size: 1.25rem; vertical-align: middle; margin-right: 1rem"
      ></i>
      {{ isFollowing ? '언팔로우' : '팔로우' }}
    </button>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import AvatarSrc from '@/assets/avatar.png'
import { followApi } from '@/apis/userApi'
import { useUserStore } from '@/stores/userStore'
import { RouterLink } from 'vue-router'

const props = defineProps(['user', 'isCurrentUser'])

const route = useRoute()
const router = useRouter()

const userStore = useUserStore()

const userId = route.params.userId
const userProfilePic = (path) => `http://localhost:8000${path}`
const loggedInUserId = parseInt(localStorage.getItem('userPk'))

// following logic
const isFollowing = ref(false)

const checkFollowing = () => {
  isFollowing.value = props.user.followers.some((follower) => follower.id === loggedInUserId)
}

watchEffect(() => {
  checkFollowing()
})

const followUnfollow = () => {
  const token = localStorage.getItem('token')

  // 로그인 안 한 경우 redirect
  if (!userStore.isLogin) {
    const userConfirmation = window.confirm(
      '로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?'
    )
    if (userConfirmation) {
      router.push({ name: 'userLogin' })
    }
    return
  }

  followApi(token, userId)
    .then((response) => {
      if (response.status === 200) {
        props.user.followers = response.data.followers
        props.user.followings = response.data.followings
        isFollowing.value = response.data.followers.some(
          (follower) => follower.id === loggedInUserId
        )
        props.user.follower_count = response.data.follower_count
      }
    })
    .catch((error) => {
      console.error('Error following/unfollowing user:', error)
    })
}
</script>

<style scoped>
.following-info {
  margin-top: 3rem;
  width: 60%;
  padding: 20px;
}

.follow-info {
  display: flex;
  justify-content: space-between;
  gap: 2rem;
  padding: 1rem;
}

.follow-info .col-md-5 {
  background-color: #fff;
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}

.text-center {
  font-weight: 700;
  color: #333;
  margin-bottom: 1.5rem;
  font-size: 1.2em;
}

.list-group {
  margin-top: 20px;
}

.list-group-item {
  display: flex;
  align-items: center;
  transition: background-color 0.3s;
  padding: 10px 20px;
  border-bottom: 1px solid #ececec;
}

.list-group-item:hover {
  background-color: #e6e6e6;
}

.profile-pic {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 15px;
}

.router-link-exact-active,
.router-link-active {
  text-decoration: none;
  color: inherit;
}

.btn {
  display: block;
  width: 100%;
  margin: 20px 0;
}

.router-link-exact-active,
.router-link-active {
  text-decoration: none;
  color: inherit;
}

.follower-following-name {
  text-decoration: none !important;
  color: black;
  font-size: 1.1em;
  font-weight: bold;
}

.list-group-item a {
  text-decoration: none;
}
</style>
