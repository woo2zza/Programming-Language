<template>
  <div class="movie-detail-container">
    <div class="movie-poster">
      <img :src="getImageUrl(movie.poster_path)" alt="이미지가 없습니다" />
    </div>
    <h1 class="movie-title">{{ movie.title }}</h1>
    <div class="movie-info">
      <p><strong>개봉일:</strong> {{ movie.release_date }}</p>
      <p><strong>러닝타임:</strong> {{ movie.runtime }} 분</p>
      <p><strong>예산:</strong> ${{ movie.budget.toLocaleString() }}</p>
      <p><strong>매출:</strong> ${{ movie.revenue.toLocaleString() }}</p>
      <p><strong>TMDB 평점:</strong> {{ movie.vote_average }} / 10</p>
    </div>
    <div class="movie-genres">
      <h3>장르</h3>
      <ul class="genre-list">
        <li v-for="genre in movie.genres" :key="genre.name">{{ genre.name }}</li>
      </ul>
    </div>
    <div class="movie-overview">
      <h3>줄거리</h3>
      <p>{{ movie.overview }}</p>
    </div>
    <div class="movie-actors">
      <h3>출연진</h3>
      <ul class="actor-list">
        <li v-for="actor in movie.actors" :key="actor.pk">
          <img :src="getImageUrl(actor.profile_path)" alt="Actor Image" class="actor-image" />
          {{ actor.name }}
        </li>
      </ul>
    </div>
    <div class="movie-youtube">
      <h3>공식 예고편</h3>
      <button
        type="button"
        class="btn"
        @click="openModal"
        data-bs-toggle="modal"
        data-bs-target="#youtubeTrailerModal"
      >
        <img :src="youtubeLogo" alt="YouTube" class="youtube-logo" />
      </button>
      <YoutubeTrailerModal :movieTitle="movie.title" />
    </div>
    <button
      :class="{ 'btn-outline-info': isPicked, 'btn-info': !isPicked }"
      class="btn mt-5 mb-5"
      style="width: 500px"
      @click="addToMyPickList"
    >
      {{ isPicked ? 'Unpick' : 'Pick' }}
    </button>
    <div class="movie-articles mt-5">
      <h1 class="text-center mb-5">게시판</h1>
      <ul style="margin-bottom: 100px">
        <li class="article-list" v-for="article in articleStore.articles" :key="article.id">
          <MovieArticleCard :article="article" style="cursor: pointer" />
        </li>
      </ul>
      <MovieArticleInput />
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { addListMovie } from '@/apis/movieApi'
import { useUserStore } from '@/stores/userStore'
import { usePickStore } from '@/stores/pickListStore'
import { useArticleStore } from '@/stores/articleStore'
import youtubeLogo from '@/assets/youtubeLogo.svg'
import MovieArticleCard from '@/components/movie/MovieArticleCard.vue'
import MovieArticleInput from '@/components/movie/MovieArticleInput.vue'
import YoutubeTrailerModal from '@/components/youtube/YoutubeTrailerModal.vue'

const props = defineProps(['movie'])

const router = useRouter()

const userStore = useUserStore()
const pickStore = usePickStore()
const articleStore = useArticleStore()

onMounted(() => {
  if (userStore.isLogin) {
    pickStore.initializePickList()
  }
  articleStore.initializeArticles(props.movie.id)
})

const getImageUrl = (path) => {
  if (!path) {
    return
  }
  return `https://image.tmdb.org/t/p/w500${path}`
}

// pick logic
const isPicked = computed(() => {
  if (userStore.isLogin && pickStore.pickList) {
    return pickStore.pickList.some((m) => m.id === props.movie.id)
  } else {
    return false
  }
})

const addToMyPickList = () => {
  if (!userStore.isLogin) {
    const userConfirmation = window.confirm(
      '로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?'
    )
    if (userConfirmation) {
      router.push({ name: 'userLogin' })
    }
    return
  }

  addListMovie(props.movie.id || props.movie.pk)
    .then((response) => {
      pickStore.addPick(props.movie)
    })
    .catch((error) => {
      console.error('Error adding to list', error)
    })
}
</script>

<style scoped>
.movie-detail-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 5rem;
}

.movie-poster img {
  margin-bottom: 80px;
  max-width: 500px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.movie-title {
  margin-top: 20px;
  font-size: 24px;
  font-weight: bold;
}

.movie-info {
  margin-top: 20px;
  text-align: center;
}

.movie-genres,
.movie-overview,
.movie-actors {
  margin-top: 30px;
  width: 70%;
  text-align: center;
}

.actor-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
}

.actor-list li {
  list-style-type: none;
  margin-bottom: 3rem;
}

.actor-image {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 10px;
}
.genre-list {
  display: flex;
  justify-content: center;
  gap: 15px;
  list-style-type: none;
  padding-left: 0;
}

.genre-list li {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.movie-articles {
  margin-top: 30px;
  width: 70%;
}

.article-list {
  list-style-type: none;
  padding-left: 0;
  /* display: flex;
  flex-direction: column; */
}

.youtube-logo {
  width: 36px;
  height: 36px;
}

.movie-youtube {
  margin-top: 20px;
  padding-left: 10rem;
  padding-right: 10rem;
  text-align: center;
  margin-bottom: 10px;
}
</style>
