<script lang="ts">
	import logo from './ldn-logo.svg';
	import { variables } from '$lib/utils/constants';
	import { locations } from '$lib/store/locationStore';

	import { userData } from '$lib/store/userStore';
	import { logOutUser } from '$lib/utils/requestUtils';
	import { onMount } from 'svelte';

	let locationList: Array<any>;
	let locationPromise: Promise<any> = Promise.resolve([]);
	async function fetchLocations(): Promise<any[]> {
		const res = await self.fetch(`${variables.BASE_MAIN_URI}/vehicles/locations/`);
		if (res.ok) {
			return res.json();
		} else {
			throw new Error('Something went wrong');
		}
	}
	onMount(() => {
		locationPromise = fetchLocations();
		locationPromise.then((data) => {
			locations.set(data);
			locations.subscribe((value) => {
				locationList = value;
			});
		});
	});
</script>

<header>
	<nav class="nav nav__main">
		<div class="nav-logo-wrapper">
			<a href="/">
				<img src={logo} alt="" style="max-height:2rem;" />
			</a>
		</div>

		<form method="get">
			<div class="nav__search--wrapper">
				<div class="form-group select location">
					<i class="icon ti ti-map-pin" />
					<select name="location" id="location" class="form-control">
						{#await locationPromise}
							<option value="">Loading...</option>
						{:then}
							{#each locationList as location}
								<option value={location.city}>{location.city}</option>
							{/each}
						{:catch}
							<option value="">Select Location</option>
						{/await}
						<!-- {#each locationList as location}
							<option value={location}>{location.toUpperCase()}</option>
						{/each} -->
					</select>
				</div>
				<div class="form-group">
					<input type="date" name="startDate" id="startDate" class="form-control" />
				</div>
				<div class="form-group">
					<input type="date" name="endDate" id="endDate" class="form-control" />
				</div>
				<div class="button-group">
					<button class="btn btn-global btn--primary">Search</button>
				</div>
			</div>
		</form>
		<div class="nav__rt-wrapper fl-row gap-2 al-center">
			<div class="nav__notification-group notification-main">
				<button class="btn btn-round-md btn--grey notification-base">
					<i class="ti ti-bell" />
				</button>
				<div class="notification-drop">
					<ul class="notification-list" />
				</div>
			</div>
			{#if !$userData.phone_number}
				<div class="button-wrapper fl-row gap-2 al-center">
					<a sveltekit:prefetch class="btn btn-global btn--grey" href="/accounts/register"
						>Register</a
					>
					<a sveltekit:prefetch class="btn btn-global btn--primary" href="/accounts/login">Login</a>
				</div>
			{:else}
				<a sveltekit:prefetch href="/accounts/user/{$userData.phone_number}-{$userData.id}">
					<div class="nav__user--group user__main dropdown-main">
						<div class="nav__user--dropdown user__base dropdown-base">
							<div class="user__base--image dropdown-base--image">
								<!-- <img src="images/user.png" alt="User" /> -->
							</div>
							<div class="user__base--text dropdown-base--text">{$userData.phone_number}</div>
							<div class="user__base--icon dropdown-base--icon">
								<i class="ti ti-chevron-down" />
							</div>
						</div>
						<div class="user__drop dropdown-drop active">
							<ul class="user__options dropdown-options">
								<li class="user__option--item dropdown-option--item">
									<a href="/" class="user__option--link dropdown-option--link">
										<span class="user__option--text dropdown-option--text">Settings</span>
										<span class="user__option--icon dropdown-option--icon"
											><i class="ti ti-settings" /></span
										>
									</a>
								</li>
								<li class="user__option--item dropdown-option--item">
									<a
										href="/"
										class="user__option--link dropdown-option--link"
										on:click={logOutUser}
									>
										<span class="user__option--text dropdown-option--text">Logout</span>
										<span class="user__option--icon dropdown-option--icon"
											><i class="ti ti-logout" /></span
										>
									</a>
								</li>
							</ul>
						</div>
					</div>
				</a>
			{/if}
		</div>
	</nav>
</header>
