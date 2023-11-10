<template>
  <div>
    <div style="position: fixed; width: 100%; z-index: 1;">
      <el-menu mode="horizontal" default-active="1" @select="handleSelect">
        <el-menu-item index="0">piapia</el-menu-item>
        <el-menu-item index="1">24</el-menu-item>
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
            <el-button size="small">签到</el-button>
          </el-badge>
          <el-button size="small" style="position: absolute; top: 25%; left: 130px;">充值</el-button>
        </span>
      </el-menu>
    </div>
  </div>
</template>

<script>
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
      }
    },
    created() {
      this.currentUser();
    }
  }
</script>
