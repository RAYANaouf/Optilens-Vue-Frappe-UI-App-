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
      class="fixed top-0 left-0 h-screen w-64 bg-white shadow-2xl z-50 transition-all duration-500 ease-out flex flex-col"
      :class="{ '-translate-x-full': !sidebarOpen, 'translate-x-0': sidebarOpen }"
    >
      <div class="p-4 flex flex-col h-full">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-xl font-bold text-gray-900">Filtering</h2>
          <button
            @click="sidebarOpen = false"
            class="text-gray-500 hover:text-gray-700"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        <!-- Filters -->
        <div class="space-y-2 overflow-y-auto flex-1">
          <!-- Company Filter -->
          <div class="border border-gray-200 rounded-lg">
            <button
              @click="toggleSection('company')"
              class="w-full flex items-center justify-between p-3 bg-gray-50 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <span class="font-medium text-gray-700">By Company</span>
              <svg
                class="w-5 h-5 text-gray-500 transition-transform"
                :class="{ 'rotate-180': openSections.company }"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
              </svg>
            </button>
            <div v-show="openSections.company" class="p-2 space-y-2">
              <label v-for="company in ($resources.filterData.data?.companies || [])" :key="company" class="flex items-center space-x-2 cursor-pointer hover:bg-gray-50 p-1 rounded">
                <input
                  type="checkbox"
                  v-model="filters.companies"
                  :value="company"
                  class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                />
                <span class="text-sm text-gray-700">{{ company }}</span>
              </label>
            </div>
          </div>

          <!-- Warehouse Filter -->
          <div class="border border-gray-200 rounded-lg">
            <button
              @click="toggleSection('warehouse')"
              class="w-full flex items-center justify-between p-3 bg-gray-50 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <span class="font-medium text-gray-700">By Warehouse</span>
              <svg
                class="w-5 h-5 text-gray-500 transition-transform"
                :class="{ 'rotate-180': openSections.warehouse }"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
              </svg>
            </button>
            <div v-show="openSections.warehouse" class="p-2 space-y-2">
              <p v-if="filters.companies.length === 0" class="text-sm text-gray-500 italic">
                Select a company first
              </p>
              <p v-else-if="filteredWarehouses.length === 0" class="text-sm text-gray-500 italic">
                No warehouses for selected companies
              </p>
              <label v-for="warehouse in filteredWarehouses" :key="warehouse.name" class="flex items-center space-x-2 cursor-pointer hover:bg-gray-50 p-1 rounded">
                <input
                  type="checkbox"
                  v-model="filters.warehouses"
                  :value="warehouse.name"
                  class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                />
                <span class="text-sm text-gray-700">{{ warehouse.name }}</span>
              </label>
            </div>
          </div>

          <!-- Brand Filter -->
          <div class="border border-gray-200 rounded-lg">
            <button
              @click="toggleSection('brand')"
              class="w-full flex items-center justify-between p-3 bg-gray-50 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <span class="font-medium text-gray-700">By Brand</span>
              <svg
                class="w-5 h-5 text-gray-500 transition-transform"
                :class="{ 'rotate-180': openSections.brand }"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
              </svg>
            </button>
            <div v-show="openSections.brand" class="p-2 space-y-2">
              <label v-for="brand in ($resources.filterData.data?.brands || [])" :key="brand" class="flex items-center space-x-2 cursor-pointer hover:bg-gray-50 p-1 rounded">
                <input
                  type="checkbox"
                  v-model="filters.brands"
                  :value="brand"
                  class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                />
                <span class="text-sm text-gray-700">{{ brand }}</span>
              </label>
            </div>
          </div>

          <!-- Group Filter -->
          <div class="border border-gray-200 rounded-lg">
            <button
              @click="toggleSection('group')"
              class="w-full flex items-center justify-between p-3 bg-gray-50 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <span class="font-medium text-gray-700">By Group</span>
              <svg
                class="w-5 h-5 text-gray-500 transition-transform"
                :class="{ 'rotate-180': openSections.group }"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
              </svg>
            </button>
            <div v-show="openSections.group" class="p-2 space-y-2">
              <label v-for="group in ($resources.filterData.data?.groups || [])" :key="group" class="flex items-center space-x-2 cursor-pointer hover:bg-gray-50 p-1 rounded">
                <input
                  type="checkbox"
                  v-model="filters.groups"
                  :value="group"
                  class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                />
                <span class="text-sm text-gray-700">{{ group }}</span>
              </label>
            </div>
          </div>

          <button
            @click="applyFilters"
            class="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition-colors"
          >
            Apply Filters
          </button>
        </div>
      </div>
    </div>

    <!-- Main Layout: Side section + Main section -->
    <div class="flex h-screen">
      <!-- Side Section - Fixed width sidebar with filters -->
      <div class="w-64 bg-transparent flex flex-col pt-6">
        <div class="flex-1 overflow-y-auto p-4">
          <!-- Filter Button -->
          <button
            @click="sidebarOpen = !sidebarOpen"
            class="w-full mb-4 bg-blue-600 text-white px-4 py-3 rounded-lg hover:bg-blue-700 transition-colors flex items-center justify-center"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"></path>
            </svg>
            Open Filters
          </button>

        </div>
      </div>

      <!-- Main Section - Matrix -->
      <div class="flex-1 p-6 overflow-hidden flex flex-col">
        <!-- Exit Button -->
        <div class="flex justify-end mb-4">
          <button
            @click="$router.push('/dashboard')"
            class="bg-red-600 text-white px-6 py-2 rounded-lg hover:bg-red-700 transition-colors flex items-center"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
            </svg>
            Exit
          </button>
        </div>

        <!-- CLY x SPH Matrix -->
        <div class="bg-white rounded-xl overflow-hidden border border-gray-200 flex-1 flex flex-col">
        <div class="overflow-auto flex-1">
          <table class="w-full text-sm border-collapse">
            <thead class="sticky top-0 z-20">
              <tr>
                <th class="px-3 py-3 sticky left-0 z-30 font-bold text-xs uppercase tracking-wider border-r border-gray-300" style="background-color: #EAEBEF; color: #374151;">SPH \ CLY</th>
                <th v-for="cly in clyValues" :key="cly" class="px-2 py-3 text-center min-w-[60px] font-semibold text-xs border-r border-gray-300 last:border-r-0" style="background-color: #EAEBEF; color: #374151;">
                  {{ cly.toFixed(2) }}
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(sph, sphIndex) in sphValues" :key="sph" :class="sphIndex % 2 === 0 ? 'bg-white' : 'bg-gray-50'">
                <th class="px-3 py-2.5 sticky left-0 z-10 font-semibold text-xs border-r border-gray-300" style="background-color: #EAEBEF; color: #374151;">{{ sph.toFixed(2) }}</th>
                <td
                  v-for="cly in clyValues"
                  :key="cly"
                  class="px-2 py-2.5 text-center border-r border-b border-gray-100 cursor-pointer hover:bg-gray-100 transition-colors"
                  :class="getCellValue(sph, cly) > 0 ? 'bg-emerald-50' : ''"
                  @click="handleCellClick(sph, cly)"
                >
                  <div class="w-full h-full flex items-center justify-center min-h-[32px] font-semibold text-sm rounded px-1" :class="getCellValue(sph, cly) > 0 ? 'text-emerald-700' : (getCellValue(sph, cly) < 0 ? 'text-red-600' : 'text-gray-300')">
                    {{ getCellValue(sph, cly) !== 0 ? getCellValue(sph, cly) : '-' }}
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { frappeRequest } from 'frappe-ui'

export default {
  name: 'Stock',
  data() {
    return {
      sidebarOpen: false,
      clyValues: this.generateValues(),
      sphValues: this.generateValues(),
      openSections: {
        company: false,
        warehouse: false,
        brand: false,
        group: false,
      },
      filters: {
        companies: [],
        warehouses: [],
        brands: [],
        groups: [],
      },
    }
  },
  resources: {
    filterData: {
      url: 'optilens_vue.api.get_filter_options',
      auto: true,
    },
    stockMatrix: {
      url: 'optilens_vue.api.get_stock_matrix',
      auto: false,
      onSuccess(data) {
        console.log('===>Stock Matrix Data:', data)
        console.log('===>Filters Applied:', data.filters_applied)
        console.log('===>Matrix:', data.matrix)
        console.log('===>Matrix Keys:', Object.keys(data.matrix || {}))
        console.log('===>Total Items:', data.items?.length)
        console.log('===>Total Qty:', data.total_qty)
        // Check first few items for SPH/CLY values
        if (data.items?.length > 0) {
          console.log('===>First 3 items:', data.items.slice(0, 3))
          // Check for SPH/CLY in custom fields
          data.items.slice(0, 5).forEach((item, idx) => {
            console.log(`===>Item ${idx} custom fields:`, {
              item_code: item.item_code,
              custom_sph: item.custom_sph,
              custom_cly: item.custom_cly,
              allKeys: Object.keys(item).filter(k => k.includes('sph') || k.includes('cly') || k.includes('sph') || k.includes('cyl'))
            })
          })
        }
      },
      onError(error) {
        console.error('>>--->Error fetching stock matrix:', error)
      },
    },
  },
  computed: {
    filteredWarehouses() {
      const allWarehouses = this.$resources.filterData.data?.warehouses || []
      if (this.filters.companies.length === 0) {
        return []
      }
      return allWarehouses.filter(w => this.filters.companies.includes(w.company))
    },
  },
  methods: {
    generateValues() {
      const values = []
      for (let i = 0; i <= 20; i += 0.25) {
        values.push(i)
      }
      return values
    },
    toggleSection(section) {
      this.openSections[section] = !this.openSections[section]
    },
    handleCellClick(sph, cly) {
      console.log(`Clicked cell: SPH=${sph.toFixed(2)}, CLY=${cly.toFixed(2)}`)
      alert(`SPH: ${sph.toFixed(2)}, CLY: ${cly.toFixed(2)}`)
    },
    async applyFilters() {
      console.log('>>> applyFilters called')
      const params = {
        companies: this.filters.companies,
        warehouses: this.filters.warehouses,
        brands: this.filters.brands,
        groups: this.filters.groups,
      }
      console.log('>>> Sending params:', params)
      
      try {
        const response = await frappeRequest({
          url: '/api/method/optilens_vue.api.get_stock_matrix',
          params: params
        })
        console.log('>>> API Response:', response)
        
        // Store the data manually
        this.$resources.stockMatrix.data = response
        console.log('>>> Stock Matrix Data:', response)
        console.log('>>> Matrix Keys:', Object.keys(response.matrix || {}))
        console.log('>>> Total Items:', response.items?.length)
        console.log('>>> Total Qty:', response.total_qty)
      } catch (error) {
        console.error('>>> API Error:', error)
        alert('API Error! Check console.')
      }
      
      this.sidebarOpen = false
    },
    getCellValue(sph, cly) {
      const matrix = this.$resources.stockMatrix.data?.matrix || {}
      const key = `${sph}_${cly}`
      const value = matrix[key] || 0
      // Debug logging for first few cells
      if (sph === 0 && cly === 0) {
        console.log('Matrix lookup:', { sph, cly, key, value, availableKeys: Object.keys(matrix).slice(0, 10) })
      }
      return value
    },
  },
}
</script>
