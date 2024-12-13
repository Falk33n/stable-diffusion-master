<script lang="ts">
	import { AppSidebar as SidebarProvider } from '$components/sections';
	import { H1, P } from '$components/typography';

	import '$src/app.css';

	let { children } = $props();
</script>

<SidebarProvider>
	<div class="w-full">
		<div
			class="bg-sidebar border-sidebar-border flex h-fit w-full justify-center border-b py-12 pl-[calc(3rem+2rem)] pr-8"
		>
			<header class=" flex flex-col gap-2">
				<H1 class="mb-4">Stable Diffusion Image Generator</H1>
				<P
					class="font-medium before:mr-2 before:content-['—'] [&:not(:first-child)]:mt-0"
				>
					Select your settings from the options in the sidebar.
				</P>
				<P
					class="font-medium before:mr-2 before:content-['—'] [&:not(:first-child)]:mt-0"
				>
					Enter a prompt that describes the image you want to generate.
				</P>
				<P
					class="font-medium before:mr-2 before:content-['—'] [&:not(:first-child)]:mt-0"
				>
					Let the model generate your image.
				</P>
				<P
					class="font-medium before:mr-2 before:content-['—'] [&:not(:first-child)]:mt-0"
				>
					Choose to either download the image or generate a new image.
				</P>
			</header>
		</div>

		<main class="bg-red-100 py-12 pl-[calc(3rem+2rem)] pr-8">
			{@render children?.()}
		</main>
	</div>
</SidebarProvider>
