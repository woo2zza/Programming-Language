<template>
  <div id="headerCarousel" class="carousel slide container-fluid mt-1" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img :src="header1" class="d-block w-100" alt="Header 1" />
      </div>
      <div class="carousel-item">
        <img :src="header2" class="d-block w-100" alt="Header 2" />
      </div>
      <div class="carousel-item">
        <img :src="header3" class="d-block w-100" alt="Header 3" />
      </div>
    </div>
    <button
      class="carousel-control-prev"
      type="button"
      data-bs-target="#headerCarousel"
      data-bs-slide="prev"
    >
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button
      class="carousel-control-next"
      type="button"
      data-bs-target="#headerCarousel"
      data-bs-slide="next"
    >
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script setup>
// 대문 페이지에 들어가는 사진 3장을 carousel로 출력
import header1 from '@/assets/header1.jpg'
import header2 from '@/assets/header2.jpg'
import header3 from '@/assets/header3.jpg'
</script>

<style scoped>
#headerCarousel,
.carousel-inner {
  width: 100%;
}

.carousel-item img {
  /* height: 100vh;
  object-fit: cover; */
}
</style>
