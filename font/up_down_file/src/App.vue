<!--<template>-->
<!--  <div>-->
<!--    <form enctype="multipart/form-data">-->
<!--      <input type="file"  multiple @change="onFileChange">-->
<!--      <button @click="upload">Upload</button>-->
<!--    </form>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import axios from 'axios'-->

<!--export default {-->
<!--  data() {-->
<!--    return {-->
<!--      file: null-->
<!--    }-->
<!--  },-->

<!--  methods: {-->
<!--    onFileChange(e) {-->
<!--      this.file = e.target.files-->
<!--      // console.log(this.file)-->
<!--    },-->

<!--    async upload() {-->
<!--      for (let i = 0; i < this.file.length; i++) {-->
<!--        let fordata = new FormData()-->
<!--        fordata.append('file', this.file[i])-->
<!--        console.log(fordata)-->
<!--        let {data} = await axios.post("http://127.0.0.1:5000/upload", fordata,)-->

<!--        this.$emit('uploaded', data.filename)-->
<!--      }-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->



<script setup>
import {ref} from 'vue'
import axios  from "axios";
const files = ref([])

// 选择文件时添加到数组
function onFileChange(e) {
  files.value.push(...e.target.files)
}

// 上传文件
async function uploadFiles() {
  const promises = []

  for (let file of files.value) {
    let formData = new FormData()
    formData.append('file', file)

    promises.push(axios.post('http://127.0.0.1:5000/upload', formData,))
  }

  await Promise.all(promises)

  console.log('All files uploaded')
}

</script>

<template>
<input type="file" multiple @change="onFileChange">
<button @click="uploadFiles">Upload All</button>
</template>



