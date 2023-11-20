<template>
  <div>
    <div style="position: fixed; width: 100%; z-index: 1;">
      <el-menu mode="horizontal" default-active="1" @select="handleSelect">
        <el-menu-item index="0">piapia</el-menu-item>
        <el-menu-item index="1">21</el-menu-item>
        <el-submenu index="2">
          <template slot="title">排行</template>
          <el-menu-item index="2-1">选项1</el-menu-item>
          <el-menu-item index="2-2">选项2</el-menu-item>
          <el-menu-item index="2-3">选项3</el-menu-item>
          <el-menu-item index="2-4">选项4</el-menu-item>
        </el-submenu>
        <span style="width: 200px; height: 100%; position: absolute; right: 0%;">
          <el-avatar style="position: absolute; top: 20%; left: 0;">{{ name }}</el-avatar>
          <el-badge is-dot style="position: absolute; top: 25%; left: 60px;">
            <el-button size="small" @click="clockIn">签到</el-button>
          </el-badge>
          <el-button size="small" style="position: absolute; top: 25%; left: 130px;" type="danger" @click="logout">退出</el-button>
        </span>
      </el-menu>
    </div>
  </div>
</template>

<script>
import router from '@/router'
  export default {
    data() {
      return {
        userId: '',
        name: ''
      };
    },
    methods: {
      currentUser() {
        this.$axios.get('/auth/current_user').then(resp => {
          localStorage.setItem('name', resp.data.name);
          localStorage.setItem('userId', resp.data.user_id);
          this.userId = resp.data.user_id;
          this.name = resp.data.name;
        })
      },
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
      logout() {
        this.$axios.get('/auth/logout').then(resp => {
          this.$message({
            message: '你已退出当前用户',
            type: 'success'
          });
          router.push('/login');
        })
      },
      clockIn() {
        this.$message({
          message: '你点了一下签到，这并没有什么卵用',
        })
      }
    },
    created() {
      this.currentUser();
    }
  }
</script>
