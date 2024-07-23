<script lang="ts">
import Task from '../models/task'
export default {
  props: ['isOpen'],
  data() {
    return {
      formData: {
        title: '',
        startDate: '',
        endDate: ''
      }
    }
  },
  methods: {
    handleSubmit() {
      console.log('emitting submit')
      this.$emit('submit', {
        name: this.formData.title,
        dateStart: this.formData.startDate ? new Date(this.formData.startDate) : null,
        dateEnd: this.formData.startDate ? new Date(this.formData.endDate) : null
      } as Task)
      this.closeDialog()
    },
    closeDialog() {
      this.$emit('close')
    }
  }
}
</script>

<template>
  <div v-if="isOpen" class="dialog-overlay">
    <div class="dialog">
      <h3>Form</h3>
      <form @submit.prevent.stop="handleSubmit">
        <label for="title">Name:</label>
        <input type="text" v-model="formData.title" id="title" required />

        <label for="startDate">Start date:</label>
        <input type="date" v-model="formData.startDate" id="startDate" />

        <label for="endDate">End date:</label>
        <input type="date" v-model="formData.endDate" id="endDate" />

        <button type="submit">Submit</button>
        <button type="button" @click="closeDialog">Cancel</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.dialog {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>
