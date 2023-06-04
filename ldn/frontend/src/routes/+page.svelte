<script lang="ts">
	import type { VehicleSmall } from '$lib/interfaces/vehicles.interface';
	import { loading } from '$lib/store/loadingStore';
	import { userData } from '$lib/store/userStore';
	import { variables } from '$lib/utils/constants';
	import { logOutUser } from '$lib/utils/requestUtils';
	import { onMount } from 'svelte';
	import { get } from 'svelte/store';
	import { fly } from 'svelte/transition';
	let vehicleList: Promise<VehicleSmall[]> = Promise.resolve([]);

	async function fetchVehicles() {
		const res = await self.fetch(`${variables.BASE_MAIN_URI}/vehicles/open-vehicles/`);
		if (res.ok) {
			return res.json();
		} else {
			throw new Error('Something went Wrong');
		}
	}
	onMount(() => {
		document.body.classList.add('overflow-hidden');
		vehicleList = fetchVehicles();
	});
</script>

<svelte:head>
	<title>LDN | Home</title>
</svelte:head>
<div class="full-height row overflow-hidden w-100">
	<section class="filter--options col-lg-2">
		<h3 class="heading-5 mb-xs">Filters</h3>
		<div class="filter-wrapper">
			<div class="filter-group">
				<div class="label">Region Lock</div>
				<div class="form-group">
					<label for="filterInside"
						>Inside Area Only <input type="checkbox" name="filterInside" id="filterInside" /></label
					>
				</div>
				<div class="form-group">
					<label for="filterOutside"
						>Inside & Outside Area
						<input type="checkbox" name="filterOutside" id="filterOutside" /></label
					>
				</div>
			</div>
			<div class="filter-group">
				<div class="label">Transmission</div>

				<div class="form-group">
					<label for="filterAutomatic"
						>Automatic <input type="checkbox" name="filterAutomatic" id="filterAutomatic" /></label
					>
				</div>
				<div class="form-group">
					<label for="filterManual"
						>Manual <input type="checkbox" name="filterManual" id="filterManual" /></label
					>
				</div>
			</div>
			<div class="filter-group">
				<div class="label">Fuel</div>
				<div class="form-group">
					<label for="filterElectric"
						>Electric <input type="checkbox" name="filterElectric" id="filterElectric" /></label
					>
				</div>
				<div class="form-group">
					<label for="filterDiesel"
						>Diesel <input type="checkbox" name="filterDiesel" id="filterDiesel" /></label
					>
				</div>
				<div class="form-group">
					<label for="filterPetrol"
						>Petrol <input type="checkbox" name="filterPetrol" id="filterPetrol" /></label
					>
				</div>
				<div class="form-group">
					<label for="filterHybrid"
						>Hybrid <input type="checkbox" name="filterHybrid" id="filterHybrid" /></label
					>
				</div>
			</div>
			<div class="filter-group">
				<div class="label">Mileage</div>
				<div class="fl-row">
					<div class="form-group">
						<label for="filterMileageStart"
							>From
							<input
								type="number"
								id="filterMileageStart"
								name="filterMileageStart"
								class="form-control"
							/>
						</label>
					</div>
					<div class="form-group">
						<label for="filterMileageEnd"
							>To
							<input
								type="number"
								id="filterMileageEnd"
								name="filterMileageEnd"
								class="form-control"
							/>
						</label>
					</div>
				</div>
			</div>
			<div class="filter-group">
				<div class="label">Seats</div>
				<div class="fl-row">
					<div class="form-group">
						<label for="filterSeatsStart"
							>From
							<input
								type="number"
								id="filterSeatsStart"
								name="filterSeatsStart"
								class="form-control"
								value="2"
							/>
						</label>
					</div>
					<div class="form-group">
						<label for="filterSeatsEnd"
							>To
							<input type="number" id="filterSeatsEnd" name="filterSeatsEnd" class="form-control" />
						</label>
					</div>
				</div>
			</div>
		</div>
		<div class="filter-wrapper">
			<div class="heading-5 wrapper--title">Filter by Car</div>
			<div class="filter-group">
				<div class="form-group">
					<label for="filterSedan"
						>Sedan <input type="checkbox" name="filterSedan" id="filterSedan" /></label
					>
				</div>
				<div class="form-group">
					<label for="filterSUV"
						>SUV <input type="checkbox" name="filterSUV" id="filterSUV" /></label
					>
				</div>
				<div class="form-group">
					<label for="filterTruck"
						>Truck <input type="checkbox" name="filterTruck" id="filterTruck" /></label
					>
				</div>
				<div class="form-group">
					<label for="filterVan"
						>Van <input type="checkbox" name="filterVan" id="filterVan" /></label
					>
				</div>
				<div class="form-group">
					<label for="filterMotorcycle"
						>Motorcycle <input
							type="checkbox"
							name="filterMotorcycle"
							id="filterMotorcycle"
						/></label
					>
				</div>
				<div class="form-group">
					<label for="filterBus"
						>Bus <input type="checkbox" name="filterBus" id="filterBus" /></label
					>
				</div>
			</div>
			<div class="filter-group" />
		</div>
	</section>
	<section class="main__list--wrapper col-lg-10">
		<div class="main__list--view-switcher fl-row jc-between al-center">
			<h2 class="heading-5 page-title">Showing Result for Vehicles</h2>
			<ul class="main__list--view-options fl-row al-center gap-2">
				<li class="main__list--view-item">
					<button class="main__list--view-link btn btn--grey btn-icon-md">
						<i class="ti ti-grid-dots" />
					</button>
				</li>
				<li class="main__list--view-item">
					<button class="main__list--view-link btn btn--grey btn-icon-md">
						<i class="ti ti-list" />
					</button>
				</li>
			</ul>
		</div>
		<div class="main__list--row row al-start">
			{#await vehicleList}
				loading...
			{:then vehicles}
				{#each vehicles as vehicle}
					<div class="col-6 col-md-4 col-lg-3">
						<div class="vehicle__card">
							<div class="location--wrapper">
								{vehicle.location_area ? 'Inside Area Only' : 'Inside & Outside Area'}
							</div>
							<div class="vehicle__card--image df-image-wrapper">
								<img src={vehicle.vehicle_image} alt="{vehicle.model_name} Image" />
							</div>
							<div class="vehicle__card--price-wrapper">
								Rs. {parseInt(vehicle.vehicle_daily_price)}
							</div>

							<div class="vehicle__card--text-wrapper">
								<h4 class="heading-4 title-wrapper">
									{vehicle.model_manufacturer}
									{vehicle.model_name}
								</h4>
								<div class="heading-5 primary">
									<div class="primary">{vehicle.reg_no.toUpperCase()}</div>
								</div>

								<div class="vehicle__bound">{vehicle.vehicle_location}, {vehicle.vehicle_city}</div>
								<div class="vehicle__card--spec-grid py-xs">
									<div class="spec-group group-row">
										<div class="spec-title">Color:</div>
										<div class="spec-value">
											<div class="color-value">
												<div class="color-circle" style="--color: #{vehicle.color_code}" />
												{vehicle.color_name}
											</div>
										</div>
									</div>
									<div class="spec-group group-row">
										<div class="spec-title">Seats <i class="ti ti-users" /></div>
										<div class="spec-value">{vehicle.seats} Seats</div>
									</div>
									<div class="spec-group group-row">
										<div class="spec-title">Transmission <i class="ti ti-hexagon" /></div>
										<div class="spec-value">{vehicle.transmission}</div>
									</div>
									<div class="spec-group group-row">
										<div class="spec-title">Mileage <i class="ti ti-hexagon" /></div>
										<div class="spec-value">
											{vehicle.mileage}
											{vehicle.fuel_type === 'EV' ? 'KM/Ch' : 'KM/L'}
										</div>
									</div>
								</div>

								<div class="vehicle__card--action-group">
									<a href="/{vehicle.slug}" class="btn btn-global btn--grey">Check Out</a>
									<button class="btn btn-global btn--primary">Book Now</button>
								</div>
							</div>
						</div>
					</div>
				{/each}
			{/await}
		</div>
	</section>
</div>
