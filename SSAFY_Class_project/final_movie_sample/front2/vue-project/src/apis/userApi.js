import axios from "axios";
import Swal from "sweetalert2";

const API_URL = "http://127.0.0.1:8000";

export const signUpApi = (payload) => {
  return axios
    .post(`${API_URL}/accounts/signup/`, payload)
    .then((response) => {
      return response;
    })
    .catch((error) => {
      if (error.response && error.response.data) {
        const errorData = error.response.data;
        let errorMessage = "";

        Object.values(errorData).forEach((messages) => {
          const translatedMessages = messages
            .map(translateMessage)
            .filter(Boolean);
          errorMessage += `${translatedMessages.join(", ")}<br>`;
        });

        if (errorMessage) {
          Swal.fire({
            title: "회원가입 에러",
            html: errorMessage,
            icon: "error",
            confirmButtonColor: "#682cd48c",
            confirmButtonText: "확인",
          });
        }
      } else {
        console.error("알 수 없는 에러가 발생했습니다.", error);
      }
    });
};

const translateMessage = (message) => {
  const translations = {
    "User with this username already exists.": "이미 존재하는 아이디입니다.",
    "This password is too common.": "비밀번호가 너무 단순합니다.",
  };
  return translations[message] || "";
};

// 로그인
export const loginApi = (payload) => {
  return axios
    .post(`${API_URL}/accounts/login/`, payload)
    .then((response) => {
      return response;
    })
    .catch((error) => {
      console.error("API 요청 중 에러가 발생했습니다:", error);
      throw error;
    });
};

// 로그아웃
export const logoutApi = () => {
  return axios
    .post(`${API_URL}/accounts/logout/`)
    .then((response) => {
      return response;
    })
    .catch((error) => {
      console.error("API 요청 중 에러가 발생했습니다:", error);
      throw error;
    });
};

// 로그인 & 회원가입 후 유저 정보 조회
export const userProfileApi = (userPk) => {
  return axios
    .get(`${API_URL}/profile/${userPk}/`)
    .then((response) => {
      return response;
    })
    .catch((error) => {
      console.error("API 요청 중 에러가 발생했습니다:", error);
      throw error;
    });
};

// 다른 유저 정보 조회
export const fetchCurrentUserApi = (token) => {
  return axios
    .get(`${API_URL}/accounts/user/`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
    .then((response) => {
      return response;
    })
    .catch((error) => {
      console.error("API 요청 중 에러가 발생했습니다:", error);
      throw error;
    });
};

// 팔로우, 언팔로우 API
export const followApi = (token, userPk) => {
  return axios
    .post(
      `${API_URL}/profile/${userPk}/follow/`,
      {},
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    )
    .then((response) => {
      return response;
    })
    .catch((error) => {
      console.error("API 요청 중 에러가 발생했습니다:", error);
      throw error;
    });
};

// 프로필 사진 변경 api
export const profilePicEdit = (userPk, payload) => {
  const token = window.localStorage.getItem("token");

  return axios
    .put(`${API_URL}/profile/${userPk}/update/`, payload, {
      headers: {
        "Content-Type": "multipart/form-data",
        Authorization: `Token ${token}`,
      },
    })
    .then((response) => {
      return response;
    })
    .catch((error) => {
      console.error("API 요청 중 에러가 발생했습니다:", error);
      throw error;
    });
};
