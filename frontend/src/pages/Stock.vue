<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Sidebar Backdrop -->
    <div
      @click="sidebarOpen = false"
      class="fixed inset-0 bg-black bg-opacity-50 z-50 transition-opacity duration-300"
      :class="{ 'opacity-0 pointer-events-none': !sidebarOpen, 'opacity-100 pointer-events-auto': sidebarOpen }"
    ></div>

    <!-- Sidebar -->
    <div
      class="fixed top-0 left-0 h-full w-64 bg-white shadow-2xl z-50 transition-all duration-500 ease-out"
      :class="{ '-translate-x-full': !sidebarOpen, 'translate-x-0': sidebarOpen }"
    >
      <div class="p-4">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-xl font-bold text-gray-900">Menu</h2>
          <button
            @click="sidebarOpen = false"
            class="text-gray-500 hover:text-gray-700"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        <nav class="space-y-2">
          <Link
            to="/"
            class="flex items-center px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
            </svg>
            Dashboard
          </Link>
          <Link
            to="/pos"
            class="flex items-center px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
            </svg>
            POS
          </Link>
          <Link
            to="/pricing"
            class="flex items-center px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            Pricing
          </Link>
        </nav>
      </div>
    </div>

    <!-- Stock Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Sidebar Toggle Button -->
      <button
        @click="sidebarOpen = !sidebarOpen"
        class="mb-4 bg-blue-600 text-white px-4 py-2 rounded-lg shadow-lg hover:bg-blue-700 transition-colors flex items-center"
      >
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
        Menu
      </button>

      <!-- CLY x SPH Matrix -->
      <div class="bg-white rounded-lg shadow">
        <div class="overflow-auto max-h-[70vh]">
          <table class="w-full text-sm">
            <thead>
              <tr>
                <th class="px-2 py-2 bg-gray-100 sticky left-0 z-10">SPH \ CLY</th>
                <th v-for="cly in clyValues" :key="cly" class="px-2 py-2 bg-gray-100 text-center min-w-[60px]">
                  {{ cly.toFixed(2) }}
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="sph in sphValues" :key="sph" class="border-b">
                <th class="px-2 py-2 bg-gray-100 sticky left-0 z-10 font-medium">{{ sph.toFixed(2) }}</th>
                <td
                  v-for="cly in clyValues"
                  :key="cly"
                  class="px-2 py-2 text-center border cursor-pointer hover:bg-blue-50 transition-colors"
                  @click="handleCellClick(sph, cly)"
                >
                  <div class="w-full h-full flex items-center justify-center min-h-[30px]">
                    0
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Stock',
  data() {
    return {
      sidebarOpen: false,
      clyValues: this.generateValues(),
      sphValues: this.generateValues(),
    }
  },
  methods: {
    generateValues() {
      const values = []
      for (let i = 0; i <= 20; i += 0.25) {
        values.push(i)
      }
      return values
    },
    handleCellClick(sph, cly) {
      console.log(`Clicked cell: SPH=${sph.toFixed(2)}, CLY=${cly.toFixed(2)}`)
      // You can add custom logic here, e.g., show a modal, edit quantity, etc.
      alert(`SPH: ${sph.toFixed(2)}, CLY: ${cly.toFixed(2)}`)
    },
  },
}
</script>
