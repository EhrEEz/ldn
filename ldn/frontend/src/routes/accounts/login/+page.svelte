<script lang="ts">
	import { notificationData } from '$lib/store/notificationStore';
	import { post, browserSet, browserGet } from '$lib/utils/requestUtils';
	import { goto } from '$app/navigation';
	import { variables } from '$lib/utils/constants';
	import { fly } from 'svelte/transition';

	import type { UserResponse } from '$lib/interfaces/user.interface';
	import type { CustomError } from '$lib/interfaces/error.interface';
	import { changeText } from '$lib/helpers/buttonText';

	let phone_number = '',
		password = '',
		errors: Array<CustomError>;

	const handleLogin = async () => {
		if (browserGet('refreshToken')) {
			localStorage.removeItem('refreshToken');
		}
		const [jsonRes] = await post(fetch, `${variables.BASE_API_URI}/login/`, {
			user: {
				phone_number: phone_number,
				password: password
			}
		});
		const response: UserResponse = jsonRes;
		const err = jsonRes.error ? jsonRes.error : [];
		if (err.length > 0) {
			errors = err;
		} else if (response.user) {
			if (response.user.tokens && response.user.tokens.refresh) {
				browserSet('refreshToken', response.user.tokens.refresh);
			}
			notificationData.update(() => 'Login successful...');
			await goto('/');
		}
	};
</script>

<svelte:head>
	<title>LDN Login</title>
</svelte:head>
<div
	class="center-block"
	in:fly={{ x: -100, duration: 500, delay: 500 }}
	out:fly={{ duration: 500 }}
>
	<div class="login-wrapper p-ms">
		<h1 class="heading-4">Login to LDN</h1>
		<form on:submit|preventDefault={handleLogin} class="login-form py-sm">
			<div class="form-group">
				<label for="phoneNumber">Phone Number</label>
				<input
					bind:value={phone_number}
					name="phone_number"
					type="text"
					aria-label="Phone Number"
					placeholder="Phone Number"
					required
					class="form-control"
				/>
			</div>
			<div class="form-group">
				<label for="password">Password</label>
				<input
					bind:value={password}
					name="password"
					type="password"
					aria-label="password"
					placeholder="password"
					required
					class="form-control"
				/>
			</div>
			<div class="form-group">
				<a href="#" class="ar-link fp-link">Forgot Password?</a>
			</div>
			<div class="form-group">
				<label for="remember">
					<input type="checkbox" name="remember" id="remember" class="checkbox" />
					Remember Me</label
				>
			</div>
			<a href="/accounts/register">Get started</a>
			<div class="button-group fl-row al-center jc-center gap-2">
				<button
					class="btn btn-global btn--primary"
					type="submit"
					on:click={(e) => changeText(e, 'Signing in...')}>Login</button
				>
			</div>
		</form>
	</div>
</div>
