<template>
  <div style="position: absolute; transform: translate(-50%, -50%); top: 50%; left: 50%; width: 25%;">
    <div>
      <el-form ref="form" label-position="left" :model="loginInfo" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="loginInfo.username"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="loginInfo.userpass" show-password></el-input>
        </el-form-item>
        <el-button type="primary" style="width: 100%;" @click="login">登录</el-button>
      </el-form>
    </div>
  </div>
</template>
<script>
export default {
  name: 'login',
  data () {
    return {
      loginInfo: {
        username: '',
        userpass: ''
      }
    }
  },
  methods: {
    login() {
      this.$axios.post('api/auth/login', this.loginInfo).then(resp => {
        this.$router.push('/')
      })
    }
  }
}
</script>
