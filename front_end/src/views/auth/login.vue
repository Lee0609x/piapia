<template>
  <div>
    <div style="position: absolute; transform: translate(-50%, -50%); top: 50%; left: 50%; width: 25%;">
      <div>
        <el-form ref="form" label-position="left" :model="loginInfo" @keyup.enter.native="login" label-width="80px">
          <el-form-item label="用户名">
            <el-input v-model="loginInfo.username"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input v-model="loginInfo.userpass" show-password></el-input>
          </el-form-item>
          <el-button type="primary" style="width: 100%;" @click="login">登录</el-button>
          <br/>
          <el-button type="success" style="width: 100%;" @click="registerDialog">注册</el-button>
        </el-form>
      </div>
    </div>
    <el-dialog title="注册用户" :visible.sync="dialogFormVisible">
      <el-form :model="registerInfo" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="registerInfo.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" show-password>
          <el-input v-model="registerInfo.userpass"></el-input>
        </el-form-item>
        <el-form-item label="用户昵称">
          <el-input v-model="registerInfo.nickname"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="register">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
export default {
  name: 'login',
  data () {
    return {
      dialogFormVisible: false,
      loginInfo: {
        username: '',
        userpass: ''
      },
      registerInfo: {
        nickname: '',
        username: '',
        userpass: ''
      }
    }
  },
  methods: {
    login() {
      this.$axios.post('/auth/login', this.loginInfo).then(resp => {
        this.$router.push('/');
      })
    },
    registerDialog() {
      this.registerInfo = {
        nickname: '',
        username: '',
        userpass: ''
      };
      this.dialogFormVisible = true
    },
    register() {
      this.$axios.post('/auth/register', this.registerInfo).then(resp => {
        this.$message({
          message: '注册成功',
          type: 'success'
        })
        this.dialogFormVisible = false;
        this.$router.push('/');
      })
    }
  }
}
</script>
