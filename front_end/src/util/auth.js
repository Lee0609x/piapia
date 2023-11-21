import Cookies from 'js-cookie'
const nameMark = 'name'
const idMark = 'userId'
const cookieKey = 'session'

export function loginMark(data) {
  localStorage.setItem(nameMark, data.name);
  localStorage.setItem(idMark, data.user_id);
}
export function removeLoginMark() {
  localStorage.removeItem(nameMark);
  localStorage.removeItem(idMark);
  Cookies.remove(cookieKey);
}
export function getToken() {
  Cookies.get(cookieKey);
}