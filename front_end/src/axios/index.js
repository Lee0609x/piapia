import axios from 'axios'
import { Message } from 'element-ui'

const simpleAxios = axios.create({
  baseURL: process.env.BASE_URL,
  timeout: 5000
});
simpleAxios.defaults.headers.post['Content-Type'] = 'application/json'
simpleAxios.interceptors.response.use((resp) => {
  if(resp.data.code >= 500) {
    Message({
      message: resp.data.message,
      type: 'error'
    });
    return Promise.reject('业务异常')
  }
  if(resp.data.code === 401) {
    this.$router.push('/login')
  }
})
export default simpleAxios;
