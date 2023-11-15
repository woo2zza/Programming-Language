<template>
  <nav class="navbar sticky-top" style="background-color: #e3f2fd;">
    <div class="container-fluid">
      <!-- 로고를 클릭시 홈으로 이동 -->
      <RouterLink to="/" class="navbar-brand">
        <img :src="logoSrc" alt="Logo" height="30" />
      </RouterLink>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav ms-auto d-flex">
          <RouterLink to="/movies" class="nav-link" active-class="active-tab"
            >영화목록</RouterLink
          >
          <RouterLink to="/movies/recommended" class="nav-link" active-class="active-tab"
            >영화추천</RouterLink
          >
          <!-- 로그인 된 경우 -->
          <RouterLink
            v-if="userStore.isLogin"
            :to="`/user/profile/${userStore.userData.pk}`"
            class="nav-link"
            active-class="active-tab"
          >
            프로필
          </RouterLink>
          <RouterLink
            v-if="userStore.isLogin"
            to="/logout"
            class="nav-link"
            active-class="active-tab"
          >
            로그아웃
          </RouterLink>
          <!-- 로그인 안 된 경우 -->
          <RouterLink
            v-if="!userStore.isLogin"
            to="/user/login"
            class="nav-link"
            active-class="active-tab"
          >
            로그인
          </RouterLink>
          <RouterLink
            v-if="!userStore.isLogin"
            to="/user/signup"
            class="nav-link"
            active-class="active-tab"
          >
            회원가입
          </RouterLink>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import logoSrc from '@/assets/ssafy.png'
import { useUserStore } from '@/stores/userStore'

const userStore = useUserStore()
</script>

<style scoped>
/* .custom-navbar-bg {
  background-color: rgb(194, 209, 211) !important;
} */

.active-tab {
  color: green !important;
  font-weight: bold !important;
}
</style>
