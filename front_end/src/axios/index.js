import axios from 'axios'
import { Message } from 'element-ui'
import router from '@/router'

const simpleAxios = axios.create({
  baseURL: process.env.BASE_URL,
  withCredentials: true,
  timeout: 5000
});
simpleAxios.defaults.headers.post['Content-Type'] = 'application/json'
simpleAxios.interceptors.response.use((resp) => {
  if (resp.data.code === 0) {
    return resp.data;
  }
  if(resp.data.code >= 500) {
    Message({
      message: resp.data.message,
      type: 'error'
    });
    return Promise.reject('业务异常');
  }
  if(resp.data.code === 401) {
    Message({
      message: '用户未登录或登录超时，请重新登录'
    });
    router.push('/login');
  }
})
export default simpleAxios;
