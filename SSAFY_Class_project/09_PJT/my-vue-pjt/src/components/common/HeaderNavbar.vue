<template>
  <header>
    <nav class="navbar navbar-expand-lg ">
      <div class="contents">
        <RouterLink to="/" class="navbar-brand" >
        <img :src="logo" alt="Logo" height="80" class="d-inline-block align-text-top" /> 
        </RouterLink>
      </div>

      <div class=" navbar-collapse " id="navbarNavAltMarkup">
        <ul class="navbar-nav ms-auto d-flex">
          <h3><RouterLink to="/movies" class="nav-link" active-class="active-tab"><strong>영화조회</strong></RouterLink></h3>
          <h3><RouterLink to="/review-search" class="nav-link" active-class="active-tab"><strong>리뷰검색</strong></RouterLink></h3>
          <h3><RouterLink to="/recommended" class="nav-link" active-class="active-tab"><strong>영화추천</strong></RouterLink></h3>
        </ul>
      </div>
    </nav>
  </header>
<hr>
</template>

<script setup>
import { ref } from 'vue'
import logoSrc from '@/assets/movie_logo.png'

const logo = ref(logoSrc)
</script>



<style scoped>


.active-tab {
  color: rgb(148, 140, 71) !important;
}
</style>
